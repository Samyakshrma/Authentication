from app.database import users_collection
from app.models import UserCreate
from app.auth import hash_password
from typing import Optional

# Create user in DB
def create_user(user: UserCreate):
    user_dict = user.dict()
    user_dict['password'] = hash_password(user.password)
    result = users_collection.insert_one(user_dict)
    return str(result.inserted_id)

# Get user by email
def get_user_by_email(email: str):
    return users_collection.find_one({"email": email})

# Get user by ID
def get_user_by_id(user_id: str):
    return users_collection.find_one({"_id": user_id})

# Update user
def update_user(user_id: str, user_data: dict):
    users_collection.update_one({"_id": user_id}, {"$set": user_data})

# Delete user
def delete_user(user_id: str):
    users_collection.delete_one({"_id": user_id})
