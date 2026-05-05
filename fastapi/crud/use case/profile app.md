# Scenario: "User Profile App"

User can:
* register
* view profile
* update profile
* delete account

## 1. CREATE (POST) — Register user

**UI action:**
User fills form → clicks “Register”

**POST /users**

**What API does:**
* receives user data
* stores in database

**Flow:**
UI → POST /users → API → DB INSERT → API → response

**Output:**
```json
{
  "message": "user created",
  "id": 1
}
```

## 2. READ (GET) — View profile

**UI action:**
User opens profile page

**GET /users/1**

**Flow:**
UI → GET /users/1 → API → DB SELECT → API → UI

**Output:**
```json
{
  "id": 1,
  "name": "John"
}
```

## 3. UPDATE (PUT) — Edit profile

**UI action:**
User updates name

**PUT /users/1**

**Flow:**
UI → PUT /users/1 → API → DB UPDATE → API → UI

**Output:**
```json
{
  "message": "updated",
  "data": {
    "id": 1,
    "name": "John Updated"
  }
}
```

## 4. DELETE — Remove account

**UI action:**
User clicks “Delete account”

**DELETE /users/1**

**Flow:**
UI → DELETE /users/1 → API → DB DELETE → API → UI

**Output:**
```json
{
  "message": "user deleted"
}
```

## FULL SYSTEM CYCLE (IMPORTANT)

1. POST → create user in DB
2. GET → read user from DB
3. PUT → update user in DB
4. DELETE → remove user from DB

## Key intuition (this is the important part)

Endpoints are NOT isolated. They form a state lifecycle:
**CREATE → READ → UPDATE → DELETE**

## One mental model

Think of a user as an object in a system:
* **POST** = object appears
* **GET** = object is viewed
* **PUT** = object is modified
* **DELETE** = object disappears

## What you are really learning

Not endpoints. But this:
**How a system changes state through HTTP requests**
