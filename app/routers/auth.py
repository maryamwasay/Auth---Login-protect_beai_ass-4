from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel

from app.database import supabase
from app.middleware.auth_middleware import verify_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# -----------------------------
# Request Body Model
# -----------------------------
class UserAuth(BaseModel):
    email: str
    password: str


# -----------------------------
# Signup
# -----------------------------
@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: UserAuth):

    if not user.email or not user.password:
        raise HTTPException(
            status_code=400,
            detail="Email and password are required"
        )

    try:

        response = supabase.auth.sign_up(
            {
                "email": user.email,
                "password": user.password
            }
        )

        return {
            "message": "User created successfully",
            "user": response.user
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# -----------------------------
# Login
# -----------------------------
@router.post("/login", status_code=status.HTTP_200_OK)
def login(user: UserAuth):

    if not user.email or not user.password:
        raise HTTPException(
            status_code=400,
            detail="Email and password are required"
        )

    try:

        response = supabase.auth.sign_in_with_password(
            {
                "email": user.email,
                "password": user.password
            }
        )

        return {
            "access_token": response.session.access_token,
            "refresh_token": response.session.refresh_token
        }

    except Exception as e:
        raise HTTPException(
        status_code=401,
        detail=str(e)
    )


# -----------------------------
# Logout
# -----------------------------
@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(user=Depends(verify_user)):

    supabase.auth.sign_out()

    return
