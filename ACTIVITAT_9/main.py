from fastapi import FastAPI
from schemas.schema import User
from crud.read import read_users

app = FastAPI()

@app.get("/users/", response_model=list[User])
def get_users():
    return read_users()