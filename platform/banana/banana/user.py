from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=128, null=True)


User = pydantic_model_creator(Users, name="User", exclude=('password',))
UserIn = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)
UserInternal = pydantic_model_creator(Users, name="UserInternal")
