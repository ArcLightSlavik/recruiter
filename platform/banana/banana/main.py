from fastapi import FastAPI
from fastapi import Request

from fastapi.responses import JSONResponse
from tortoise.contrib.fastapi import register_tortoise

from . import user_api
from . import resource_api
from .exceptions import CredentialsException
from .postgres_db import TortoiseSettings


app = FastAPI()
app.include_router(user_api.user_router)
app.include_router(resource_api.resource_router)


@app.on_event("startup")
def startup():
    config = TortoiseSettings.generate()
    register_tortoise(
        app,
        db_url=config.db_url,
        generate_schemas=config.generate_schemas,
        modules=config.modules,
    )


@app.exception_handler(CredentialsException)
def credentials_exception_handler(_request: Request, _exc: CredentialsException):
    return JSONResponse(
        status_code=401,
        content=dict(message="Could not validate credentials"),
        headers={"WWW-Authenticate": "Bearer"},
    )
