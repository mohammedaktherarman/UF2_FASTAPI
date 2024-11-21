from pydantic import BaseModel

class User(BaseModel):
    user_id: int
    user_name: str
    user_surname: str
    user_age: int
    user_email: str
