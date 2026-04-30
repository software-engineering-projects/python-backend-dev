```
Project Prompt: FastAPI Backend Learning Build

We are building a simple backend system using Python and FastAPI to learn how real-world APIs work.

Goal
• Create a minimal CRUD (Create, Read, Delete) API
• Store and manage data in memory
• Understand backend fundamentals:
  • routing
  • request handling
  • validation
  • data flow

What we are building

A basic API that can:

1. Create data (POST /data)
• Accept JSON input
• Store it in memory

2. Read data (GET /data)
• Return all stored items

3. Delete data (DELETE /data/{id})
• Remove an item by ID

Tech stack
• Python
• FastAPI (web framework)
• Uvicorn (server)

Core concept being learned

• How APIs receive requests
• How routes map to functions
• How data flows:
  • client → server → response
• How in-memory storage works (temporary state)
• How CRUD operations are structured in backend systems

Current state of the project

• FastAPI app is running locally
• POST endpoint accepts JSON data
• GET endpoint returns stored items
• DELETE endpoint removes items by ID
• Data is stored in memory (resets on restart)

Next planned improvements

• Auto-generate unique IDs
• Prevent duplicate entries
• Add update (PUT/PATCH) endpoint
• Introduce persistent storage (file or database)
```
