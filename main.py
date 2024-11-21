from fastapi import FastAPI
from src.routes.router import router
app = FastAPI()

# Create the tables automatically when the app starts
# Base.metadata.create_all(bind=engine)

# Include authentication routes
app.include_router(router)