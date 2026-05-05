# Data Transformation: Database Rows to JSON Objects

### The Problem

The `GET /profile` endpoint was returning raw PostgreSQL output in a tuple/list format:

```json
{
  "data": [
    [1, "John", 25],
    [2, "Test User", 25]
  ]
}
```

**Issues with this format:**
*   Data was in tuple/list format rather than structured objects.
*   Structure came directly from the database `fetchall()` method.
*   The frontend has no context for what the values `1`, `"John"`, or `25` represent.
*   The API response was not self-descriptive.
*   It was inconsistent with the `POST` endpoint, which is JSON object-based.

### The Solution

Database rows are manually transformed into structured JSON objects.

**Before:**
```python
rows = cursor.fetchall()
return {"data": rows}
```

**After:**
```python
profiles = []
for row in rows:
    profiles.append({
        "id": row[0],
        "name": row[1],
        "age": row[2]
    })

return {
    "message": "profiles retrieved successfully",
    "data": profiles
}
```

**Key Changes:**
*   Converted tuples into dictionaries.
*   Added semantic meaning to each field:
    *   `row[0]` becomes `id`
    *   `row[1]` becomes `name`
    *   `row[2]` becomes `age`
*   Standardized the API response format.

### Importance of Data Transformation

This implementation follows core backend engineering principles:

#### 1. Separation of Concerns
Database format ≠ API format ≠ UI format.
*   **Database**: Stores raw rows optimized for storage.
*   **API**: Reshapes data optimized for communication.
*   **UI**: Consumes readable JSON optimized for humans.

#### 2. Frontend Usability
The frontend can now access data using descriptive keys (e.g., `profile.name`) instead of unclear indices (e.g., `data[0][1]`).

#### 3. API Consistency
The mismatch between endpoints has been resolved:

| Endpoint | Format Before | Format After |
| :--- | :--- | :--- |
| POST | JSON object | JSON object |
| GET | Raw tuples | JSON object |

#### 4. Real-world Readiness
This is standard behavior for production APIs:
*   Prevents raw database leakage.
*   Ensures all responses are structured.
*   The frontend does not depend on the database schema.
*   The backend maintains control over the data shape.

#### 5. Foundation for Scaling
This step is required before adding advanced features such as:
*   Authentication (users/login)
*   Frontend frameworks (React, Vue)
*   API versioning
*   Microservices
*   Data validation layers (Pydantic / schemas)

### Final Mental Model

**BEFORE:**
PostgreSQL → raw rows → UI (confusing, unsafe)

**AFTER:**
PostgreSQL → FastAPI (transform) → JSON API → UI (clean, predictable)
