# Create First Database Table

### Step 1: Create the table
Inside `profile_db`, execute the following SQL command:

```sql
CREATE TABLE profiles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT
);
```

### Step 2: Verify table creation
Run the following command to ensure the table exists:

```sql
SELECT * FROM profiles;
```
*Note: An empty result set is expected at this stage.*

### Step 3: Insert test data
Add a sample record to the table:

```sql
INSERT INTO profiles (name, age)
VALUES ('John Doe', 25);
```

### Step 4: Check data
Run the selection query again to verify the record was added:

```sql
SELECT * FROM profiles;
```
**Expected Result:**
You should now see one row containing the data for "John Doe".
