import orm

from . import postgres_db


class NoteModel(orm.Model):
    __tablename__ = "notes"
    __database__ = postgres_db.database
    __metadata__ = postgres_db.metadata

    id = orm.Integer(primary_key=True)
    text = orm.String(max_length=100)
    completed = orm.Boolean(default=False)
