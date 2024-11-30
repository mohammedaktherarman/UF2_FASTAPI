from pydantic import BaseModel

class Tematica(BaseModel):
    option: str

class Paraula(BaseModel):
    option: str