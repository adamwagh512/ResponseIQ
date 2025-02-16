from fastapi import FastAPI
from api.samsara import fetch_vehicle_locations
from api.traumasoft import fetch_active_calls

#This script runs a FastAPI server with endpoints to trigger data fetching.

# Initialize FastAPI application
app = FastAPI()

@app.get("/")
def home():
    """ Root endpoint to confirm API is running. """
    return {"message": "ResponseIQ API is running 🚑"}

@app.get("/fetch/vehicles")
def fetch_vehicles():
    """ Fetch latest vehicle locations from Samsara API. """
    fetch_vehicle_locations()
    return {"message": "Vehicle locations updated."}

@app.get("/fetch/calls")
def fetch_calls():
    """ Fetch latest active EMS calls from Traumasoft API. """
    fetch_active_calls()
    return {"message": "Active EMS calls updated."}

# Run FastAPI server with: uvicorn main:app --reload