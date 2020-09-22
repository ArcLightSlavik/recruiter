import pydantic


class NoteIn(pydantic.BaseModel):
    text: str
    completed: bool


class Note(pydantic.BaseModel):
    id: int
    text: str
    completed: bool
