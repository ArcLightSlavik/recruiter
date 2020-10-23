from typing import Generic, Optional, Type

from pydantic import UUID4
from tortoise import fields, models
from tortoise.exceptions import DoesNotExist

from fastapi.security import OAuth2PasswordRequestForm

from .. import password
from ..models import UD


class TortoiseBaseUserModel(models.Model):
    id = fields.UUIDField(pk=True, generated=False)
    email = fields.CharField(index=True, unique=True, null=False, max_length=255)
    hashed_password = fields.CharField(null=False, max_length=255)
    is_active = fields.BooleanField(default=True, null=False)
    is_superuser = fields.BooleanField(default=False, null=False)

    async def to_dict(self):
        d = {}
        for field in self._meta.db_fields:
            d[field] = getattr(self, field)
        for field in self._meta.backward_fk_fields:
            d[field] = await getattr(self, field).all().values()
        return d

    class Meta:
        abstract = True


class TortoiseUserDatabase(Generic[UD]):
    model: Type[TortoiseBaseUserModel]

    def __init__(self, user_db_model: Type[UD], model: Type[TortoiseBaseUserModel]):
        self.user_db_model = user_db_model
        self.model = model

    async def get(self, id: UUID4) -> Optional[UD]:
        try:
            query = self.model.get(id=id)

            user = await query
            user_dict = await user.to_dict()

            return self.user_db_model(**user_dict)
        except DoesNotExist:
            return None

    async def get_by_email(self, email: str) -> Optional[UD]:
        query = self.model.filter(email__iexact=email).first()
        user = await query

        if user is None:
            return None

        user_dict = await user.to_dict()
        return self.user_db_model(**user_dict)

    async def create(self, user: UD) -> UD:
        user_dict = user.dict()

        model = self.model(**user_dict)
        await model.save()

        return user

    async def update(self, user: UD) -> UD:
        user_dict = user.dict()
        user_dict.pop("id")  # Tortoise complains if we pass the PK again

        model = await self.model.get(id=user.id)
        for field in user_dict:
            setattr(model, field, user_dict[field])
        await model.save()

        return user

    async def delete(self, user: UD) -> None:
        await self.model.filter(id=user.id).delete()

    async def authenticate(self, credentials: OAuth2PasswordRequestForm) -> Optional[UD]:
        user = await self.get_by_email(credentials.username)

        if user is None:
            # Run the hasher to mitigate timing attack
            # Inspired from Django: https://code.djangoproject.com/ticket/20760
            password.get_password_hash(credentials.password)
            return None

        verified, updated_password_hash = password.verify_and_update_password(
            credentials.password, user.hashed_password
        )
        if not verified:
            return None
        # Update password hash to a more robust one if needed
        if updated_password_hash is not None:
            user.hashed_password = updated_password_hash
            await self.update(user)

        return user
