```mermaid
flowchart LR

A[Client Request] --> B[URL: /users or /validate]
B --> C[Route Matching]

C -->|/users| D[get_users function]
C -->|/validate| E[validate_data function]

D --> F[Response: list of users]
E --> G[Response: validation result]

F --> H[Client]
G --> H
```

```js
Routes (endpoints)

• A route maps a URL → a specific function in your backend

• When a client (browser, app, API caller) hits a URL:
  • The framework checks: “Which function handles this URL?”
  • Then it runs that function

• Example:

  • /users
    → Calls a function like: get_users()
    → Returns list of users

  • /validate
    → Calls a function like: validate_data()
    → Processes and returns validation result

• Mental model:
  • URL = trigger
  • Route = mapping
  • Function = execution

• Flow:
  • Client requests /users
  • Route matches /users
  • Corresponding function runs
  • Function returns response


```
