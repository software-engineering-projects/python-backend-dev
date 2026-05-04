# What happens when you use BaseModel in a class

`class Item(BaseModel):`

You are making Item a Pydantic model.

## What this gives you

### 1. Data validation
It enforces structure:
* name → must be string
* value → must be int

### 2. Automatic parsing
Incoming JSON:
```json
{
  "name": "test",
  "value": 123
}
```

Becomes:
```python
item = Item(name="test", value=123)
```

### 3. Attribute access
Inside your function:
* `item.name`
* `item.value`

### 4. Error handling (automatic)
If input is wrong → FastAPI returns error (no manual checking needed)

## Simple mental model
`class Item(BaseModel)`
* → defines what valid data looks like
* → converts JSON → Python object
* → enforces correctness

---

# In OOP, this is called inheritance.

## What you’re doing

```python
class Item(BaseModel):
```

Means:
Item inherits from BaseModel

## What inheritance means

Child class gets behavior from parent class

So:
* BaseModel = parent
* Item = child

## What Item gains

From BaseModel, it automatically gets:
* validation
* parsing
* data handling methods

## Simple mental model

* BaseModel → provides functionality
* Item → uses and extends it
