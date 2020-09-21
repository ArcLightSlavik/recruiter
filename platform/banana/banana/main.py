import fastapi
import pydantic

from typing import Dict, List

from .postgres_db import database, notes

app = fastapi.FastAPI()


class NoteIn(pydantic.BaseModel):
    text: str
    completed: bool


class Note(pydantic.BaseModel):
    id: int
    text: str
    completed: bool


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/notes/", response_model=List[Note])
async def read_notes():
    query = notes.select()
    return await database.fetch_all(query)


@app.post("/notes/", response_model=Note)
async def create_note(note: NoteIn):
    query = notes.insert().values(text=note.text, completed=note.completed)
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}


@app.get("/")
async def read_root() -> Dict[str, str]:
    return {"msg": "Hello, World!"}


@app.get("/hello")
async def read_hello() -> Dict[str, str]:
    return {"msg": "Welcome to Banana World"}
