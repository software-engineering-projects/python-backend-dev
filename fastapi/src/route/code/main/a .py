from fastapi import FastAPI  
# Imports the FastAPI class from the fastapi library.
# FastAPI is used to create web APIs in Python.

app = FastAPI()  
# Creates an instance of the FastAPI application.
# This 'app' object is what Uvicorn will run.

@app.get("/test")  
# Defines a route (endpoint) for HTTP GET requests.
# When someone visits "/test", this function will be executed.

def test_route():  
# Defines a function that will handle requests to the "/test" endpoint.

    return {"message": "API is working"}  
# Returns a JSON response to the client.
# FastAPI automatically converts this dictionary into JSON format.
