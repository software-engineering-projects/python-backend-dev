from fastapi import FastAPI  
# Imports FastAPI, the main class used to create the API application.

from pydantic import BaseModel  
# Imports BaseModel from Pydantic.
# Pydantic is used for data validation and defining request body structure.

app = FastAPI()  
# Creates an instance of the FastAPI application.
# This object handles all routes and server behavior.

@app.get("/test")  
# Defines a GET endpoint at the path "/test".
# When a user visits this URL, the function below is executed.

def test_route():  
# Function that handles requests to "/test".

    return {"message": "API is working"}  
# Returns a JSON response confirming the API is running.


class Item(BaseModel):  
# Defines a data model using Pydantic.
# This model describes the expected structure of incoming JSON data.

    name: str  
    # Field "name" must be a string.

    value: int  
    # Field "value" must be an integer.


@app.post("/data")  
# Defines a POST endpoint at "/data".
# This endpoint expects data to be sent in the request body.

def receive_data(item: Item):  
# Function that receives request data.
# FastAPI automatically validates incoming JSON against the Item model.

    return {"received": item}  
# Returns the received data back to the client as JSON.
# FastAPI converts the Pydantic model into a JSON-compatible format.
