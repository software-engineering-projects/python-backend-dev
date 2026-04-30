from fastapi import FastAPI  
# Imports FastAPI to create the web API application.

from pydantic import BaseModel  
# Imports BaseModel for request data validation and structure.

app = FastAPI()  
# Creates the FastAPI application instance.

items = []  
# In-memory list acting as temporary storage (like a fake database).


@app.get("/test")  
# Defines a GET endpoint at "/test".

def test_route():  
# Function handling requests to "/test".

    return {"message": "API is working"}  
# Returns a simple JSON response confirming the API is running.


class Item(BaseModel):  
# Defines a data model for incoming request data.

    id: int  
    # Unique identifier for each item (integer).

    name: str  
    # Name of the item (string).

    value: int  
    # Numeric value associated with the item (integer).


@app.post("/data")  
# Defines a POST endpoint for adding new items.

def receive_data(item: Item):  
# Receives and validates incoming JSON against the Item model.

    items.append(item)  
    # Stores the validated item in the in-memory list.

    return {"message": "saved", "data": item}  
    # Returns confirmation and the saved item.


@app.get("/data")  
# Defines a GET endpoint to retrieve all stored items.

def get_data():  
# Function that returns all items.

    return items  
# Returns the full list of stored items.


@app.delete("/data/{item_id}")  
# Defines a DELETE endpoint with a path parameter.
# Example: /data/1 will pass item_id = 1

def delete_item(item_id: int):  
# Function that deletes an item based on its ID.

    for item in items:  
    # Loops through all stored items.

        if item.id == item_id:  
        # Checks if current item's ID matches the requested ID.

            items.remove(item)  
            # Removes the matching item from the list.

            return {"message": "deleted", "id": item_id}  
            # Returns success message if item is found and deleted.
    
    return {"message": "not found"}  
    # If no matching item is found, returns a not found message.
