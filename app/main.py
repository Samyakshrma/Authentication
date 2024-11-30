from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app import crud, auth, schemas, role
from app.auth import decode_access_token
from app.database import users_collection
from app.schemas import Token
from app.models import UserCreate
from typing import List
import logging

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Configure logging
logging.basicConfig(level=logging.INFO)


# Login Endpoint
@app.post("/login", response_model=Token)
def login_for_access_token(form_data: schemas.UserCreate):
    user = crud.get_user_by_email(form_data.email)
    if not user or not auth.verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = auth.create_access_token(data={"username": form_data.email, "role": user["role"]})
    return {"access_token": access_token, "token_type": "bearer"}


# Secure CRUD Endpoints
@app.post("/user/create")
def create_user(user: UserCreate, token: str = Depends(oauth2_scheme)):
    decoded_token = decode_access_token(token)
    if not decoded_token or not role.check_permission(decoded_token.role, "create"):
        raise HTTPException(status_code=403, detail="Permission denied")
    crud.create_user(user)
    return {"msg": "User created"}


@app.get("/user/{user_id}")
def read_user(user_id: str, token: str = Depends(oauth2_scheme)):
    decoded_token = decode_access_token(token)
    if not decoded_token:
        raise HTTPException(status_code=403, detail="Permission denied")
    user = crud.get_user_by_id(user_id)
    return user
