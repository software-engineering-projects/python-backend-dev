# Backend Database Integration

### What we are building now

You are upgrading from:
UI → FastAPI → return data (temporary)

to:
UI → FastAPI → PostgreSQL → stored profile (permanent)

### Goal of this step

POST /profile
* takes name + age
* inserts into profiles table
* returns success message

### Step 1 — Create real endpoint

In main.py, you will replace your test endpoint with a real one:

```python
from db import get_connection
from fastapi import FastAPI

app = FastAPI()

@app.post("/profile")
def create_profile(item: dict):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO profiles (name, age) VALUES (%s, %s)",
        (item["name"], item["age"])
    )

    conn.commit()
    conn.close()

    return {
        "message": "profile created successfully",
        "data": item
    }
```

### What each step is doing

1. Receive user input (name, age)
2. Open DB connection
3. Create cursor (to run SQL)
4. INSERT data into profiles table
5. Save changes (commit)
6. Close connection
7. Return response to UI

### Real-world mapping

| Code step | Real-world meaning |
| :--- | :--- |
| connect | open DB session |
| cursor | SQL executor |
| execute | run INSERT query |
| commit | save to DB |
| close | end session |

### Step 2 — Test it

Go to:
http://127.0.0.1:8000/docs

Then:
1. POST /profile
2. Try it out
3. Send:
```json
{
  "name": "Loyd",
  "age": 25
}
```

### Expected result

```json
{
  "message": "profile created successfully",
  "data": {
    "name": "Loyd",
    "age": 25
  }
}
```

### What changed in your system

Before:
API = temporary response generator

Now:
API = writes real data into PostgreSQL

### Important milestone you just hit

You now have:
FIRST REAL DATABASE WRITE OPERATION

This is the core of backend systems.

### Next step

If this works, we move to:
GET /profile → retrieve data from PostgreSQL

So you can see full CRUD cycle:
CREATE → READ → UPDATE → DELETE
