
# What BaseModel is used for (in your project)

It defines the structure of incoming data.

## Basic use

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    value: int
```

## What this means

You are telling FastAPI:

“I expect data with:
- name → string
- value → integer”

## Where it is used

In your POST:

```python
@app.post("/data")
def create_item(item: Item):
```

## What happens during a request

User sends JSON:
```json
{
  "name": "test",
  "value": 123
}
```

FastAPI:
* checks if it matches Item
* converts it into a Python object (item)

## If input is wrong

Example:
```json
{
  "name": "test"
}
```

→ FastAPI rejects it (missing value)

## Simple mental model

BaseModel = input validator + data structure
