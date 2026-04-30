from fastapi import FastAPI  
# Imports FastAPI, used to build the web API application.

from pydantic import BaseModel  
# Imports BaseModel for defining and validating structured request data.

app = FastAPI()  
# Creates the FastAPI application instance.

items = []  
# Creates an in-memory list to store data.
# This acts like a temporary database (data is lost when server restarts).


@app.get("/test")  
# Defines a GET endpoint at "/test".

def test_route():  
# Function that handles requests to "/test".

    return {"message": "API is working"}  
# Returns a simple JSON response to confirm the API is running.


class Item(BaseModel):  
# Defines a data model for incoming request data.

    name: str  
    # "name" must be a string.

    value: int  
    # "value" must be an integer.


@app.post("/data")  
# Defines a POST endpoint at "/data".
# Used to send data to the server.

def receive_data(item: Item):  
# Receives and validates incoming JSON data using the Item model.

    items.append(item)  
    # Adds the validated item to the in-memory list.

    return {"message": "saved", "data": item}  
    # Returns confirmation plus the saved item.


@app.get("/data")  
# Defines a GET endpoint at "/data".
# Used to retrieve all stored items.

def get_data():  
# Function that handles retrieval requests.

    return items  
# Returns the full list of stored items as JSON.
