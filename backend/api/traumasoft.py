import requests
from database import calls_collection  # Import MongoDB collection
from config import TRAUMASOFT_API_KEY  # Import API key

# This script fetches active EMS calls from Traumasoft API and stores them in MongoDB.
# Traumasoft API base URL
TRAUMASOFT_URL = "https://api.traumasoft.com/v1"

def fetch_active_calls():
    """
    Fetch active EMS calls from Traumasoft API and store them in MongoDB.
    """
    url = f"{TRAUMASOFT_URL}/calls/active"
    headers = {"Authorization": f"Bearer {TRAUMASOFT_API_KEY}"}

    # Send GET request to Traumasoft API
    response = requests.get(url, headers=headers)

    # Check for a successful response
    if response.status_code == 200:
        data = response.json()

        # Loop through each EMS call
        for call in data.get("calls", []):
            calls_collection.update_one(
                {"call_id": call["call_id"]},  # Find existing call by ID
                {"$set": call},  # Update with new data
                upsert=True  # Insert if not exists
            )
        print("✅ Active EMS calls updated successfully.")
    else:
        print("❌ Error fetching EMS calls:", response.status_code, response.text)
