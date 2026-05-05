# PUT /profile Implementation

### What we are building
PUT /profile → update an existing profile in PostgreSQL

### User story (UPDATE operation)
1. User opens profile in UI
2. User edits name or age
3. User clicks "Update Profile"
4. UI sends request: `PUT /profile/{id}`
5. FastAPI receives request
6. Backend matches: `@app.put("/profile/{id}")`
7. Backend connects to PostgreSQL
8. Runs SQL: `UPDATE profiles SET name = ..., age = ... WHERE id = ...`
9. Database updates record
10. Backend returns success response
11. UI shows "Profile updated"

### Step 1 — Create endpoint

Add this to `main.py`:

```python
@app.put("/profile/{id}")
def update_profile(id: int, item: dict):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE profiles SET name = %s, age = %s WHERE id = %s",
        (item["name"], item["age"], id)
    )

    conn.commit()
    conn.close()

    return {
        "message": "profile updated successfully",
        "id": id,
        "updated_data": item
    }
```

### What’s new here

1. **Path parameter**: `{id}` identifies which specific record to update.
2. **SQL UPDATE logic**: `UPDATE profiles SET name = ..., age = ... WHERE id = ...`. This is critical—without the `WHERE` clause, all rows would be updated.
3. **commit()**: Saves the update permanently in PostgreSQL.

### Flow comparison

| Operation | SQL behavior |
| :--- | :--- |
| POST | INSERT new row |
| GET | SELECT rows |
| PUT | UPDATE existing row |

### How to test

1. Go to: `http://127.0.0.1:8000/docs`
2. Find: `PUT /profile/{id}`
3. Click "Try it out"
4. Enter the ID (e.g., 1) and the following JSON:

```json
{
  "name": "Updated Name",
  "age": 30
}
```

### Expected result

```json
{
  "message": "profile updated successfully",
  "id": 1,
  "updated_data": {
    "name": "Updated Name",
    "age": 30
  }
}
```

### Summary
PUT is used to modify an existing database record using its unique ID.
