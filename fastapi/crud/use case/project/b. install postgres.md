# Install PostgreSQL driver

### 1. Ensure virtual environment is active

Your terminal should show:

```powershell
C:\profile-app\venv\   ✔ correct
```

If it is not active, run:

```powershell
.\venv\Scripts\Activate.ps1
```

### 2. Install package

Run:

```cmd
pip install psycopg2-binary
```

### 3. Verify installation

Run:

```cmd
pip list
```

**Look for:**
* psycopg2-binary

### Technical Details

**What you just installed:**
`psycopg2-binary` is the PostgreSQL connector for Python.

It allows FastAPI to perform the following actions on PostgreSQL:
* Connect
* Query
* Insert/Update/Delete

**Simple intuition:**
FastAPI → Python driver → PostgreSQL
