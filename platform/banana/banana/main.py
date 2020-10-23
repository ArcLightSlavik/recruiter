from fastapi import FastAPI

from tortoise.contrib.fastapi import register_tortoise

from .api import resource_api

from .exceptions import CredentialsException, credentials_exception_handler
from .postgres_db import TortoiseSettings


app = FastAPI()
app.include_router(resource_api.resource_router, tags=["resource"])

app.add_exception_handler(CredentialsException, credentials_exception_handler)

@app.on_event("startup")
def startup():
    config = TortoiseSettings.generate()
    register_tortoise(
        app,
        db_url=config.db_url,
        generate_schemas=config.generate_schemas,
        modules=config.modules,
    )


from .fast_users.router import (
    auth,
    users,
    register,
    reset
)

app.include_router(
    auth.auth_router,
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    users.users_router,
    prefix="/users",
    tags=["users"],
)

app.include_router(
    register.register_router,
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    reset.reset_router,
    prefix="/auth",
    tags=["auth"],
)
