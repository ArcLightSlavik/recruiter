from typing import List

import fastapi
import pydantic

company_router = fastapi.APIRouter()


class Company(pydantic.BaseModel):
    id: str
    name: str
    employee_number: int
    locations: List[str]
    website_url: str


items = {
    "google": {
        "id": "random_id",
        "name": "google",
        "employee_number": 10000,
        "locations": ["Lviv", "Kyiv"],
        "website_url": "google.com"
    }
}


@company_router.get("/company/{company_name}", response_model=Company)
async def get_company_by_id(company_name: str):
    return items[company_name]
