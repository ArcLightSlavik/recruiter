from typing import Dict

import fastapi

from recruiter.utils.service_config import get_info

resource_router = fastapi.APIRouter()


@resource_router.get("/")
async def get_root() -> Dict[str, str]:
    return {"message": "OK"}


@resource_router.get("/health")
async def get_health() -> Dict[str, str]:
    return {"message": "OK"}


@resource_router.get("/version")
async def get_version() -> Dict[str, str]:
    return get_info()
