from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str
    role: Optional[str] = None

class UserInDB(BaseModel):
    username: str
    email: str
    hashed_password: str

from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        # This will allow the model to parse data from the client (e.g. by not requiring extra fields).
        orm_mode = True
