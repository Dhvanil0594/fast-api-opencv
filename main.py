from fastapi import FastAPI
from src.routes.router import router

app = FastAPI()

# Include authentication routes
app.include_router(router)