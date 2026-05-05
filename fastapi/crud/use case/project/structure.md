# Project Structure

## Directory Layout

```text
profile_app/
├── Include/        # venv system files
├── Lib/            # venv system files
├── Scripts/        # venv system files
├── .gitignore      # project file
├── pyvenv.cfg      # venv config file
└── app/            # Application source code
```

## Key Rules

*   **Virtual Environment Files:** `Include/`, `Lib/`, and `Scripts/` constitute the Python environment engine. Do not modify these files; they are not part of the application logic.
*   **Application Folder:** All backend system code must reside within the `app/` directory.

## Application Structure (inside app/)

The `app/` directory contains the core project logic:

```text
app/
├── main.py
├── routes/
├── models/
├── database/
└── services/
```

## Mental Model

*   **Environment Engine:** `Include/`, `Lib/`, `Scripts/`
*   **Application Logic:** `app/`
