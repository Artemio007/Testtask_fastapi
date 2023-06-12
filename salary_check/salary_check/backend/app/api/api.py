from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from app.auth.cookie import auth_backend
from app.schemas.user import UserRead, UserCreate
from app.auth.manager import get_user_manager
from app.models.user import User


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()
api_router = APIRouter()


api_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

api_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
