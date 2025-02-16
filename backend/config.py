import os

# This file holds API keys and MongoDB settings.
# Load API keys securely from environment variables (or use defaults for testing)
SAMSARA_API_KEY = os.getenv("SAMSARA_API_KEY", "your_samsara_api_key")
TRAUMASOFT_API_KEY = os.getenv("TRAUMASOFT_API_KEY", "your_traumasoft_api_key")

# MongoDB connection URI (default is a local MongoDB instance)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")

# Name of the MongoDB database
DB_NAME = "ResponseIQ"
