import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()

users = {
    "admin": "secret123",
    "user": "password",
}


def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_password = users.get(credentials.username)
    if correct_password is None or correct_password != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверные учётные данные",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.get("/")
def public():
    return {"message": "Публичная страница"}


@app.get("/secret")
def secret(user: str = Depends(get_current_user)):
    return {"message": f"Привет, {user}! Это секретная страница"}


uvicorn.run(app, host="127.0.0.1", port=8000)
