import requests
from database import vehicle_collection  # Import MongoDB collection
from config import SAMSARA_API_KEY  # Import API key

# This script fetches real-time vehicle locations from Samsara API and stores them in MongoDB.
# Samsara API base URL
BASE_URL = "https://api.samsara.com/v1"

def fetch_vehicle_locations():
    """
    Fetch live vehicle locations from Samsara API and store them in MongoDB.
    """
    url = f"{BASE_URL}/fleet/vehicles/locations"
    headers = {"Authorization": f"Bearer {SAMSARA_API_KEY}"}

    # Send GET request to Samsara API
    response = requests.get(url, headers=headers)

    # Check for a successful response
    if response.status_code == 200:
        data = response.json()

        # Loop through each vehicle entry in the response
        for vehicle in data.get("vehicles", []):
            vehicle_collection.update_one(
                {"id": vehicle["id"]},  # Find existing vehicle by ID
                {"$set": vehicle},  # Update existing data with new info
                upsert=True  # Insert new document if vehicle ID doesn't exist
            )
        print("✅ Vehicle locations updated successfully.")
    else:
        print("❌ Error fetching vehicle locations:", response.status_code, response.text)
