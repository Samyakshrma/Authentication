from app.crud import create_user
from app.models import UserCreate

new_user = UserCreate(username="admin", email="admin@example.com", password="securepassword")
create_user(new_user)
