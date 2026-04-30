```mermaid
flowchart LR

A[Client Request] --> B[URL (/users or /validate)]
B --> C[Route Matching]

C -->|/users| D[get_users() function]
C -->|/validate| E[validate_data() function]

D --> F[Response (list of users)]
E --> G[Response (validation result)]

F --> H[Client]
G --> H
```
