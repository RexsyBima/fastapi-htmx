from pydantic import BaseModel


class UserRegister(BaseModel):
    username: str
    hobby: str
