# Application Development Template (Backend-Centered System)

This is a standard structure template for building a full-stack application (UI + API + Database), starting from backend-first design.

## 1. Project Overview

*   **Project Name:**
*   **Purpose:**
*   **Core Features:**
*   **Example use:** Profile management system, User registration and management

## 2. System Architecture

UI → API → Database → API → UI

**Layers:**
*   **UI:** user interaction layer
*   **API:** logic + request handler
*   **DB:** persistent storage

## 3. Data Model (Domain Design)

Define core entities BEFORE coding.

**Entity: User**
*   id (int)
*   name (string)
*   age (int)

**Rules:**
*   Define structure first
*   Keep it minimal
*   Avoid implementation details

## 4. API Contract (Endpoints Design)

Define what system can do.

*   **POST /register** → create user
*   **GET /user/{id}** → get user
*   **PUT /user/{id}** → update user
*   **DELETE /user/{id}** → delete user

**Rules:**
*   Endpoint = action
*   Do not implement logic yet
*   Only define behavior

## 5. Database Schema

Map data model into storage structure.

**Table: users**
*   id (Primary Key)
*   name
*   age

**Rules:**
*   Keep schema aligned with data model
*   Ensure uniqueness of ID
*   Define constraints early

## 6. Backend Design (Logic Layer)

Define responsibilities per endpoint.

*   **POST** → validate + insert into DB
*   **GET** → fetch from DB
*   **PUT** → update DB record
*   **DELETE** → remove DB record

**Rules:**
*   Backend = logic only
*   No UI concerns
*   No storage logic inside UI

## 7. UI Design (Interaction Layer)

Minimal structure:

**Pages:**
*   Register Form
*   Profile View
*   Update Form

**Responsibilities:**
*   Collect input
*   Send requests to API
*   Display responses

## 8. Data Flow Standard

UI → API → DB → API → UI

**CRUD mapping:**

| Action | Flow |
| :--- | :--- |
| Create | UI → POST → DB INSERT |
| Read | UI → GET → DB SELECT |
| Update | UI → PUT → DB UPDATE |
| Delete | UI → DELETE → DB DELETE |

## 9. Development Order (Enterprise Standard)

1.  Data Model
2.  API Contract
3.  Database Schema
4.  Backend Implementation
5.  UI Implementation
6.  Integration Testing

## 10. Core Principles

*   Backend is source of truth
*   UI is only a client
*   Database is persistent storage
*   API is the communication bridge

## 11. Minimal Viable Version Rule

Start with:
*   1 entity (User)
*   4 endpoints (CRUD)
*   1 table
*   1 simple UI form

Expand only after system is stable.
