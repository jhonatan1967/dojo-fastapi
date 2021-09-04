from fastapi import APIRouter

from app.routers.db import user

router = APIRouter()

router.include_router(user.router, prefix="/users", tags=["user"])