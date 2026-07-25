from fastapi import APIRouter, Depends

from app.middleware.auth_middleware import verify_user

router = APIRouter(
    prefix="/protected",
    tags=["Protected"]
)


@router.get("/profile")
def profile(user=Depends(verify_user)):
    return {
        "id": user.id,
        "email": user.email,
        "created_at": user.created_at
    }


@router.get("/dashboard")
def dashboard(user=Depends(verify_user)):
    return {
        "message": f"Welcome {user.email}",
        "dashboard": "This is a protected dashboard."
    }
