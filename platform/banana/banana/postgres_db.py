# from __future__ import annotations
#
# from pydantic import Field
# from pydantic import BaseSettings
#
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
# SQLALCHEMY_DATABASE_URL = "postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"
#
#
# class PostgresSettings(BaseSettings):
#     postgres_user: str = Field(env="POSTGRES_USER")
#     postgres_password: str = Field(env="POSTGRES_PASSWORD")
#     postgres_db: str = Field(env="POSTGRES_DB")
#     postgres_port: str = Field(env="POSTGRES_PORT")
#     postgres_host: str = Field(env="POSTGRES_HOST")
#
#
# class AlchemySettings:
#
#     def __init__(self):
#         self._db_url = None
#         self._alchemy_base = None
#         self._alchemy_engine = None
#         self._alchemy_session = None
#
#         self.generate()
#
#     def generate(self) -> None:
#         postgres = PostgresSettings()
#         self._alchemy_base = declarative_base()
#         self._db_url = SQLALCHEMY_DATABASE_URL.format(**postgres.dict())
#         self._alchemy_engine = create_engine(self._db_url)
#         self._alchemy_session = sessionmaker(autocommit=False, autoflush=False, bind=self._alchemy_engine)
#
#     def get_base(self):
#         if self._alchemy_base is None:
#             self.generate()
#         return self._alchemy_base
#
#     def get_engine(self):
#         if self._alchemy_engine is None:
#             self.generate()
#         return self._alchemy_engine
#
#     def get_session(self):
#         if self._alchemy_session is None:
#             self.generate()
#         return self._alchemy_session
#
#
# alchemy_settings = AlchemySettings()
#
#
# # Dependency
# def get_db():
#     db = alchemy_settings.get_session()()
#     try:
#         yield db
#     finally:
#         db.close()
