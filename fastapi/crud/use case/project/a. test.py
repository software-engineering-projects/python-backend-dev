from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def test():
    return {"info": "api is working"}

# 1. User performs an action
#    (e.g. opens a page, clicks a button)

# 2. Frontend sends request
#    GET /test

# 3. Backend receives request

# 4. FastAPI matches:
#    @app.get("/test")

# 5. Function executes:
#    test()

# 6. Response is returned to UI

@app.post("/data")
def user_data(item: dict):
    return {
        "message": "processing information",
        "data": item
    }

# USER STORY: Submit Profile Data (NO DATABASE YET)
#
# 1. User opens the Profile App UI
#    - Sees form:
#      • name
#      • age

# 2. User enters data
#    Example:
#      name = "Loyd"
#      age = 25
#
# 3. User clicks "Submit"

# 4. Frontend sends request:
#    POST /data

# 5. Backend receives request
#    FastAPI matches:
#   @app.post("/data")
#
# 6. Function executes:
#    user_data(item)

# 7. Backend does NOT store data
#    It only processes input temporarily

# 8. Backend returns response:
#    {
#        "message": "processing information",
#        "data": item
#    }

# 9. UI displays confirmation message
#    (temporary success, no persistence)

