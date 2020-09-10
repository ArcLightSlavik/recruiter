from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"msg": "Hello, World!"}


@app.get("/hello")
async def read_hello():
    return {"msg": "Welcome to Banana World"}
