import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello"}


@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}


def test_add():
    response = client.get("/add?a=3&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 8}


def test_add_negative():
    response = client.get("/add?a=-2&b=10")
    assert response.status_code == 200
    assert response.json() == {"result": 8}


pytest.main()
