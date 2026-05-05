
### STEP 1: Create project folder

Open CMD and run:

```cmd
cd C:\
mkdir profile-app
cd profile-app
```

### STEP 2: Create virtual environment named app

Inside `profile-app` run:

```cmd
python -m venv app
```

**Project Structure:**
```text
profile-app/
└── app/   <-- virtual environment
```

### STEP 3: Activate the virtual environment

If you are using CMD:

```cmd
app\Scripts\activate
```

**Expected Result:**

Your terminal should now show:
```cmd
(app) C:\profile-app>
```

### Summary of Components

*   **profile-app**: Project folder
*   **app**: Isolated Python environment (venv)

### Important Rule

From now on:
*   Install packages (FastAPI, uvicorn) inside the `(app)` environment.
*   Run your backend inside this environment only.

### STEP 4: Install FastAPI + Uvicorn

Now that your venv is active (app), run:

```cmd
pip install fastapi uvicorn
```

### STEP 5: Verify installation

Run:

```cmd
pip list
```

You should see:
* fastapi
* uvicorn

### STEP 6: Create app folder

This is where your backend code lives. Run:

```cmd
mkdir app
cd app
```

### STEP 7: Create main file

```cmd
type nul > main.py
```

### Current structure

```text
profile-app/
├── app/              <-- venv
├── app/              <-- backend code folder
│   └── main.py
```

*Note: Having the same name "app" for both the virtual environment and the code folder is normal for learning.*

### STEP 8: Run server

Go inside the backend folder:

```cmd
cd app
```

Then run:

```cmd
python -m uvicorn main:app --reload
```

### Expected result

You should see:
`Uvicorn running on http://127.0.0.1:8000`
