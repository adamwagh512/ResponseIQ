from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

# This script initializes a connection to MongoDB and creates collections.
# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Create and reference the ResponseIQ database
db = client[DB_NAME]

# Define collections (similar to tables in SQL databases)
vehicle_collection = db["vehicle_locations"]
calls_collection = db["active_calls"]

print("✅ Successfully connected to MongoDB!")
