from fastapi import FastAPI

from tortoise.contrib.fastapi import register_tortoise

from . import user_api
from .api import resource_api

from .exceptions import CredentialsException, credentials_exception_handler
from .postgres_db import TortoiseSettings


app = FastAPI()
app.include_router(user_api.user_router)
app.include_router(resource_api.resource_router)

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
