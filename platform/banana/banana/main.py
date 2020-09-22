import fastapi

from typing import Dict

from . import notes
from . import resource
from . import postgres_db

app = fastapi.FastAPI()

app.include_router(notes.notes_api)
app.include_router(resource.resource_router)

@app.on_event("startup")
async def startup():
    await postgres_db.database.connect()


@app.on_event("shutdown")
async def shutdown():
    await postgres_db.database.disconnect()
