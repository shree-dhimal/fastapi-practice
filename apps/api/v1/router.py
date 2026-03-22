from fastapi import APIRouter
from apps.api.v1.endpoints import user

api_router = APIRouter()

api_router.include_router(user.router, prefix="/users", tags=["Users"])
