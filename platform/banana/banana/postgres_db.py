import os
import databases
import sqlalchemy

DATABASE_URL = os.environ['POSTGRES_URL']

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DATABASE_URL
)
metadata.create_all(engine)
