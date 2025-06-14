from fastapi import APIRouter
from api.auth import signin, signup, refresh
from api.users import settings

router = APIRouter()
router.include_router(signin.router)
router.include_router(signup.router)
router.include_router(refresh.router)
router.include_router(settings.router)
