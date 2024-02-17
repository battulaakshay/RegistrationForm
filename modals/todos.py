from pydantic import BaseModel


class Todo(BaseModel):
    fullname: str
    email: str
    password: str
    gender: str
    phonenumber: str




