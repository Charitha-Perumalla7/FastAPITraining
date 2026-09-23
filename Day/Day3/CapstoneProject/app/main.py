from fastapi import FastAPI
from app.config import settings
from app.database import ping_database
from app.routers import users

#creating Fastapi APP instance and
# setting the title of the app to the value of APP_NAME from settings
app = FastAPI(title=settings.APP_NAME)
app.include_router(users.router)  # Include the users router in the main app

#THIS function runs once when the server starts
app.on_event("startup")
def on_startup() -> None:
    if not ping_database():
        raise RuntimeError("Could not connect to MongoDB.")
    print(f"Connected to MongoDB . APP {settings.APP_NAME}")


#basic health check API endpoin 
#confirms GET/ is running and reachable
@app.get("/",tags=["Health "])
def health_check():
    return {"Status": "Okiee","App": settings.APP_NAME}