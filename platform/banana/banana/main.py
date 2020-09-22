import fastapi

from typing import Dict

from . import notes
from . import postgres_db

app = fastapi.FastAPI()

app.include_router(notes.notes_api)


@app.on_event("startup")
async def startup():
    await postgres_db.database.connect()


@app.on_event("shutdown")
async def shutdown():
    await postgres_db.database.disconnect()


@app.get("/")
async def read_root() -> Dict[str, str]:
    return {"msg": "Hello, World!"}


@app.get("/hello")
async def read_hello() -> Dict[str, str]:
    return {"msg": "Welcome to Banana World"}
