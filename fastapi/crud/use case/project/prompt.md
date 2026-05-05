```
Project Prompt: profile_app (Full Stack Learning System)

We are building a simple full-stack Profile Application to understand how a real backend system works using FastAPI, PostgreSQL, and a basic UI.

Goal

Build a minimal system where a user can:
- Register a profile (name, age)
- View profile
- Update profile
- Delete profile

The purpose is to understand end-to-end request flow, not production-level design.

System Architecture

- UI (Frontend Form)
- FastAPI Backend (API Layer)
- PostgreSQL Database (Storage Layer)
- FastAPI Backend
- UI (Response Display)

Core Components

1. UI (Simple Interface)
- Collects user input:
  - name
  - age
- Displays user data
- Triggers actions:
  - register
  - view
  - update
  - delete

2. Backend (FastAPI)
- Acts as the logic and communication layer
- Responsible for:
  - Receiving requests from UI
  - Validating input
  - Executing CRUD operations
  - Communicating with database
  - Returning responses

3. Database (PostgreSQL)
- Acts as persistent storage
- Stores user data:
  - id | name | age
- Handles:
  - INSERT (create)
  - SELECT (read)
  - UPDATE (modify)
  - DELETE (remove)

Core CRUD Flow

Register
- UI → POST /register → API → DB INSERT → API → UI

View Profile
- UI → GET /user/{id} → API → DB SELECT → API → UI

Update Profile
- UI → PUT /user/{id} → API → DB UPDATE → API → UI

Delete Profile
- UI → DELETE /user/{id} → API → DB DELETE → API → UI

Learning Focus

- How frontend communicates with backend
- How API endpoints map to CRUD operations
- How backend interacts with a database
- How data flows through the system

Key Principle

- UI sends request → API processes logic → DB stores or retrieves data → API returns response → UI displays result

Scope

- No authentication system (for now)
- No advanced frontend frameworks
- Simple forms only
- Focus on understanding flow, not UI design
```
