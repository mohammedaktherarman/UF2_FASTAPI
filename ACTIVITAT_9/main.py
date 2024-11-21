from fastapi import FastAPI
from schema import User
from read import read_users

app = FastAPI()

@app.get("/users/", response_model=list[User])
def get_users():
    return read_users()