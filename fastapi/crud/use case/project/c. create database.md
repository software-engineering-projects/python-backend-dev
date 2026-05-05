# Create Database using pgAdmin4

### Step 1: Open pgAdmin
1. Launch pgAdmin4.
2. Log in to your PostgreSQL server (e.g., "Local Postgres").

### Step 2: Connect to server
Expand the following path in the browser tree:
**Servers** > **Local Postgres** > **Databases**

### Step 3: Create new database
1. Right-click on **Databases**.
2. Select **Create** > **Database...**

### Step 4: Fill in details
In the creation form, enter the following:
*   **Database name**: `profile_db`
*   **Owner**: `postgres` (or your default user)

Leave all other settings at their default values.

### Step 5: Save
Click the **Save** button.

### Step 6: Verify
Expand the **Databases** section in the sidebar. You should now see `profile_db` listed.
