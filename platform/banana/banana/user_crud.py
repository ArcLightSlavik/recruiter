import bcrypt

from typing import List
from typing import Union

from tortoise.exceptions import DoesNotExist
from tortoise.exceptions import IntegrityError

from .user import User
from .user import Users
from .user import UserIn
from .user import UserInternal


async def get_all_users() -> List[User]:
    return await User.from_queryset(Users.all())


async def get_user_by_id(user_id: int) -> Union[User, None]:
    try:
        return await User.from_queryset_single(Users.get(id=user_id))
    except DoesNotExist:
        return None


async def get_user_by_username(username: str) -> Union[User, None]:
    try:
        return await User.from_queryset_single(Users.get(username=username))
    except DoesNotExist:
        return None


async def internal_get_user_by_username(username: str) -> Union[UserInternal, None]:
    try:
        return await UserInternal.from_queryset_single(Users.get(username=username))
    except DoesNotExist:
        return None


async def check_user_password(user: UserIn) -> bool:
    db_user_info = await internal_get_user_by_username(user.username)
    if db_user_info is None:
        return False
    return bcrypt.checkpw(user.password.encode('utf8'), db_user_info.password.encode('utf8'))


async def create_user(user: UserIn) -> Union[User, None]:
    user_dict = create_password(user.dict(exclude_unset=True))
    try:
        user_obj = await Users.create(**user_dict)
    except IntegrityError:
        return None
    return await User.from_tortoise_orm(user_obj)


async def update_user(user_id: int, user: UserIn) -> Union[User, None]:
    db_user_info = await get_user_by_id(user_id)
    if not db_user_info:
        return None
    user_dict = create_password(user.dict(exclude_unset=True))
    await Users.filter(id=user_id).update(**user_dict)
    return await get_user_by_id(user_id)


async def delete_user(user_id: int) -> int:
    return await Users.filter(id=user_id).delete()


def create_password(user: Union[User, UserIn]) -> Union[User, UserIn]:
    password_hash = bcrypt.hashpw(user['password'].encode('utf-8'), bcrypt.gensalt())
    user['password'] = password_hash.decode('utf-8')
    return user
