from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from app.config import MONGO_URI

# Create a new MongoDB client using the provided URI
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

# Connect to the database and handle potential connection errors
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Error connecting to MongoDB:", e)

# Define the database and collections
db = client.get_database("your_database_name")  # Replace with your database name
users_collection = db.get_collection("users")  # Replace with your collection name
