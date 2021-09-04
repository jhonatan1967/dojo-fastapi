from fastapi import FastAPI
from app.db.config import server
from app.routers.api import router
app = FastAPI(title="Dojo FastAPI")
app.include_router(router,prefix="/api")

@app.on_event("startup")
async def startup_event():
    server(app)