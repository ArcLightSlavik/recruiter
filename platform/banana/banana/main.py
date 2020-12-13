from fastapi import FastAPI

from .api import resource_api

app = FastAPI()

app.include_router(resource_api.resource_router, tags=['resource'])
