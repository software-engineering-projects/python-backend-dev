
# What @app.get("/test") does

It is a route decorator.

## What it means

```python
@app.get("/test")
def test_route():
```

Means:
“When a GET request comes to /test → run test_route()”

## What method is this?

It uses the HTTP GET method

So:
GET /test

## What @app.get does internally (simple view)

It:
* Registers a URL → /test
* Associates it with a function → test_route
* Restricts it to method → GET

## Equivalent mental model

* **Route:** /test
* **Method:** GET
* **Handler:** test_route()

## Important

* @app.get → only handles GET requests
* If you send POST to /test → it won’t work
---
```
Why?

• return {"message": "API is working"}
  • This sends the response back to the client (browser / Swagger)
  • It does NOT print anything to your terminal

--------------------------------------------------

What the terminal shows instead

• Server logs (from Uvicorn), like:
  • Server started
  • Request received (GET /test)
  • Status code (200 OK)

Example:
• GET /test 200 OK

--------------------------------------------------

If you want to see something in the terminal

You need to explicitly print it:

• Inside your function:
  • print("test_route was called")

Now when you hit /test:
• Terminal → shows the print output
• Browser → still gets the JSON response

--------------------------------------------------

Mental model

• return → goes to client
• print → goes to terminal (server side)

--------------------------------------------------

So:

• Browser / Swagger:
  • {"message": "API is working"}

• Terminal:
  • Only logs unless you add print()
```
