# GET /profile Implementation

### What we are building
GET /profile → fetch all saved profiles from PostgreSQL

### Full user story (READ operation)
1. User opens "View Profiles" page in UI
2. UI sends request: `GET /profile`
3. FastAPI receives request
4. FastAPI matches: `@app.get("/profile")`
5. Backend connects to PostgreSQL
6. Runs SQL: `SELECT * FROM profiles`
7. Database returns rows
8. Backend converts rows to JSON
9. UI displays list of profiles

### Step-by-step implementation

Add this to `main.py`:

```python
from db import get_connection
from fastapi import FastAPI

app = FastAPI()

@app.get("/profile")
def get_profiles():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM profiles")
    rows = cursor.fetchall()

    conn.close()

    return {
        "message": "profiles retrieved successfully",
        "data": rows
    }
```

### What each part does
*   **SELECT * FROM profiles**: Get all records
*   **fetchall()**: Convert DB result into Python list
*   **return**: Send JSON to UI

### Important behavior change
*   **Before**: POST → writes data
*   **Now**: GET → reads stored data

### How to test
1. Go to: `http://127.0.0.1:8000/docs`
2. Find **GET /profile**
3. Click **Try it out**
4. Click **Execute**

### Expected response
```json
{
  "message": "profiles retrieved successfully",
  "data": [
    [1, "John Doe", 25]
  ]
}
```

### Important insight
Right now the data format is raw tuples from PostgreSQL. Later we will improve this into clean JSON objects (proper API format).

### What you just achieved
You now have:
*   CREATE (POST /profile)
*   READ (GET /profile)

This is your first working backend system loop.
