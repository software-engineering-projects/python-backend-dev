
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
