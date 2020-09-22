import fastapi

from typing import Dict

resource_router = fastapi.APIRouter()


@resource_router.get("/")
async def read_root() -> Dict[str, str]:
    return {"msg": "Hello, World!"}


@resource_router.get("/hello")
async def read_hello() -> Dict[str, str]:
    return {"msg": "Welcome to Banana World"}
