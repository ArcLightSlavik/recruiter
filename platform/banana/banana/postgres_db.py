from pydantic import BaseSettings
from pydantic import Field

DB_MODELS = ["banana.users.models"]
POSTGRES_DB_URL = "postgres://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"


class PostgresSettings(BaseSettings):
    postgres_user: str = Field(env="POSTGRES_USER")
    postgres_password: str = Field(env="POSTGRES_PASSWORD")
    postgres_db: str = Field(env="POSTGRES_DB")
    postgres_port: str = Field(env="POSTGRES_PORT")
    postgres_host: str = Field(env="POSTGRES_HOST")


class TortoiseSettings(BaseSettings):
    db_url: str
    modules: dict
    generate_schemas: bool

    @classmethod
    def generate(cls):
        postgres = PostgresSettings()
        db_url = POSTGRES_DB_URL.format(**postgres.dict())
        del postgres
        modules = {"models": DB_MODELS}
        return TortoiseSettings(db_url=db_url, modules=modules, generate_schemas=True)
