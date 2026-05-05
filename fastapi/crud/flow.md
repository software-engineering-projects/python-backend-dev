# Backend CRUD Flow

## Overview
This document explains how a backend API interacts with a database using standard CRUD operations. Each endpoint acts as a bridge between the client and the database.

## General Flow
Client → API → Database → API → Client

The API is responsible for translating HTTP requests into database operations and returning responses.

## 1. GET (READ)

### Role
Retrieve data from the database.

### Flow
Client → API → Database SELECT → API → Client

### Behavior
* Does not modify data
* Only queries existing records
* Returns data to client

### Database Operation
SELECT

## 2. POST (CREATE)

### Role
Insert a new record into the database.

### Flow
Client → API → Database INSERT → API → Client

### Behavior
* Accepts new data from client
* Validates input
* Creates new record
* Returns created record (often with generated ID)

### Database Operation
INSERT

## 3. PUT (UPDATE)

### Role
Modify an existing record in the database.

### Flow
Client → API → Database UPDATE → API → Client

### Behavior
* Identifies record by ID
* Replaces or updates fields
* Returns updated record

### Database Operation
UPDATE

## 4. DELETE (REMOVE)

### Role
Remove a record from the database.

### Flow
Client → API → Database DELETE → API → Client

### Behavior
* Identifies record by ID
* Permanently removes record
* Returns confirmation of deletion

### Database Operation
DELETE

## Summary Table

| Method | Purpose | Database Action | Data Change |
| :--- | :--- | :--- | :--- |
| GET | Read data | SELECT | No |
| POST | Create data | INSERT | Yes |
| PUT | Update data | UPDATE | Yes |
| DELETE | Remove data | DELETE | Yes |

## Core Principle
The API does not store data — it only mediates between the client and the database.
