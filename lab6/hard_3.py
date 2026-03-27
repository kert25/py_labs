import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

users = {
    "admin": "secret123",
    "user": "password",
}


def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_password = users.get(credentials.username)
    if correct_password is None or correct_password != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверные учётные данные",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.get("/")
def root():
    return {"message": "Перейдите на /login для авторизации"}


@app.get("/login")
def login(user: str = Depends(authenticate)):
    return {"message": f"Авторизация успешна! Привет, {user}!"}


uvicorn.run(app, host="127.0.0.1", port=8000)
