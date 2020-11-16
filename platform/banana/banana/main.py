from fastapi import FastAPI

from .api import resource_api

from .exceptions import CredentialsException, credentials_exception_handler


app = FastAPI()
app.include_router(resource_api.resource_router, tags=["resource"])

app.add_exception_handler(CredentialsException, credentials_exception_handler)
