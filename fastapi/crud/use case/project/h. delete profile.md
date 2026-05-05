# DELETE /profile Implementation

### What we are building
DELETE /profile/{id} → remove a profile from PostgreSQL

### User story (DELETE operation)
1. User opens profile list in UI
2. User clicks "Delete" on a profile
3. UI sends request: DELETE /profile/1
4. FastAPI receives request
5. Backend matches: @app.delete("/profile/{id}")
6. Backend connects to PostgreSQL
7. Runs SQL: DELETE FROM profiles WHERE id = 1
8. Database removes record
9. Backend returns success response
10. UI updates list (profile disappears)

### Step 1 — Create DELETE endpoint

Add this to main.py:

```python
@app.delete("/profile/{id}")
def delete_profile(id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM profiles WHERE id = %s",
        (id,)
    )

    conn.commit()
    conn.close()

    return {
        "message": "profile deleted successfully",
        "id": id
    }
```

### What’s happening here
1. **Path parameter**: {id} → identifies which row to delete
2. **SQL DELETE**: DELETE FROM profiles WHERE id = ...
   Note: Without WHERE → would delete EVERYTHING (critical risk)
3. **commit()**: Finalizes deletion in database

### CRUD complete now

| Operation | Endpoint | SQL |
| :--- | :--- | :--- |
| CREATE | POST /profile | INSERT |
| READ | GET /profile | SELECT |
| UPDATE | PUT /profile/{id} | UPDATE |
| DELETE | DELETE /profile/{id} | DELETE |

### What you just built (big picture)
UI <-> FastAPI <-> PostgreSQL
(Full CRUD system)

### System behavior now
Your app can now:
* create profiles
* view profiles
* update profiles
* delete profiles

This is a complete backend system lifecycle.

### Key insight (important)
You are no longer writing endpoints. You are modeling real-world actions on data.
