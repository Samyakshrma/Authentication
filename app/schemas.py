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
