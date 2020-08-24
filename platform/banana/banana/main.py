from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"msg": "Hello, World!"}


@app.get("/hello")
def read_hello():
    return {"msg": "Welcome to Banana World"}
