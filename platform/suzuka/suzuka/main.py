from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import company_api
from .api import resource_api

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:6622",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(company_api.company_router, tags=['company'])
app.include_router(resource_api.resource_router, tags=['resource'])
