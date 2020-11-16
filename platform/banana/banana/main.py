from fastapi import FastAPI

from .api import user_api
from .api import resource_api

from .postgres_db import alchemy_settings

app = FastAPI()

app.include_router(user_api.user_router, tags=['user'])
app.include_router(resource_api.resource_router, tags=['resource'])


@app.on_event("startup")
async def start_db():
    async with alchemy_settings.get_engine().begin() as conn:
        await conn.run_sync(alchemy_settings.get_base().metadata.drop_all)
        await conn.run_sync(alchemy_settings.get_base().metadata.create_all)
