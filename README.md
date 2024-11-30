## FastAPI User Authentication System with JWT and MongoDB

## Requirements

- Python 3.8+
- MongoDB (preferably MongoDB Atlas)

## Setup

1. Clone the repository.
2. Create a `.env` file with your MongoDB URI and secret key:
    ```bash
    MONGO_URI="your_mongodb_uri"
    SECRET_KEY="your_secret_key"
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the FastAPI app:
    ```bash
    uvicorn app.main:app --reload
    ```

## Endpoints

- **POST /login**: Login and receive a JWT token.
- **POST /user/create**: Create a new user (admin only).
- **GET /user/{user_id}**: Read user data (authenticated).

## Script to Create Initial User

Use the `scripts/create_user.py` to insert an initial user.

## Notes

- **RBAC**: Roles are handled in the `role.py` file, and permissions are checked for each endpoint.
