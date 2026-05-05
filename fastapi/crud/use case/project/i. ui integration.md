# Full-Stack Integration: UI to Database

### What we are building
HTML Form → FastAPI → PostgreSQL → response → HTML updates

### Step 1 — Create a UI file
Inside your `app` folder, create:
`index.html`

### Step 2 — Simple UI (no CSS)
This is your basic form:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Profile App</title>
</head>
<body>

<h2>Create Profile</h2>

<form id="profileForm">
    <input type="text" id="name" placeholder="Name" required>
    <input type="number" id="age" placeholder="Age" required>
    <button type="submit">Submit</button>
</form>

<p id="result"></p>

<script>
document.getElementById("profileForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;

    const response = await fetch("http://127.0.0.1:8000/profile", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name, age })
    });

    const data = await response.json();

    document.getElementById("result").innerText =
        data.message + " → " + JSON.stringify(data.data);
});
</script>

</body>
</html>
```

### What this UI is doing
1. User enters name + age
2. Clicks submit
3. JavaScript sends POST request to FastAPI
4. FastAPI stores data in PostgreSQL
5. Response comes back
6. UI displays result

### Important concept
HTML does NOT talk to database. Only FastAPI talks to database.

**Correct Flow:**
HTML → FastAPI → PostgreSQL

**Incorrect Flow:**
HTML → PostgreSQL

### Step 3 — Fix CORS (important)
Because the UI and API are separate origins, add this to `main.py`:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Step 4 — Run system
1. Start FastAPI:
```cmd
python -m uvicorn main:app --reload
```
2. Open `index.html` in your browser.
3. Submit the form.

### Expected result
* Form submits data.
* FastAPI receives it.
* PostgreSQL stores it.
* UI shows: `profile created successfully → {"name":"...","age":...}`

### What you just achieved
First full-stack integration (UI → API → DB)
