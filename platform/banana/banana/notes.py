import fastapi

from typing import List

from .models import notes
from .schemas import Note, NoteIn
from .postgres_db import database

notes_api = fastapi.APIRouter()


@notes_api.get("/notes/", response_model=List[Note])
async def read_notes():
    query = notes.select()
    return await database.fetch_all(query)


@notes_api.post("/notes/", response_model=Note)
async def create_note(note: NoteIn):
    query = notes.insert().values(text=note.text, completed=note.completed)
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}
