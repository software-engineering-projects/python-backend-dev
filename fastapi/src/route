1. Install required libraries
• Run:
  • pip install fastapi uvicorn

2. Create project structure
• project/
  └── main.py

3. Initialize the app
• In main.py:
  • from fastapi import FastAPI
  • app = FastAPI()

4. Create a route
• Add this below:
  • @app.get("/test")
  • def test_route():
      return {"message": "API is working"}

5. Run the server
• uvicorn main:app --reload

6. Test the route
• Open browser:
  • http://127.0.0.1:8000/test

Done condition
• You should see:
  • {"message": "API is working"}
