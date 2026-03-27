import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello FastAPI!"}


@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Привет, {name}!"}


@app.get("/square")
def square(number: int):
    return {"number": number, "square": number**2}


uvicorn.run(app, host="127.0.0.1", port=8000)
