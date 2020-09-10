import fastapi

from typing import Dict

app = fastapi.FastAPI()


@app.get("/")
async def read_root() -> Dict[str, str]:
    return {"msg": "Hello, World!"}


@app.get("/hello")
async def read_hello() -> Dict[str, str]:
    return {"msg": "Welcome to Banana World"}
