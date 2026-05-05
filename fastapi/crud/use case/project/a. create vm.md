
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

### Next Steps

Once the environment is active, the process will proceed to:
1. Install fastapi and uvicorn.
2. Create the application structure.
3. Run the first API endpoint.
