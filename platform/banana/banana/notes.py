import fastapi

from typing import List

from .models import NoteModel
from .schemas import NoteIn, Note

notes_api = fastapi.APIRouter()


@notes_api.get("/notes/", response_model=List[Note])
async def read_notes():
    return await NoteModel.objects.all()


@notes_api.post("/notes/", response_model=Note)
async def create_note(note: NoteIn):
    return await NoteModel.objects.create(text=note.text, completed=note.completed)
