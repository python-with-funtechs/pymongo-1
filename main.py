from fastapi import FastAPI
from routes.routes import all_routes

app = FastAPI()

app.include_router(all_routes)

