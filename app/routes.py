from fastapi import APIRouter, Depends, HTTPException, status
from app.auth import supabase
from app.dependencies import get_current_user
from app.models import AuthRequest


router = APIRouter()


# ============================================================
# SIGN UP
# ============================================================

@router.post("/auth/signup", status_code=status.HTTP_201_CREATED)
def signup(data: AuthRequest):
    """
    Create a new user account using Supabase Auth.
    """

    # Validate required fields
    if not data.email or not data.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email and password are required"
        )

    try:
        print(f"Attempting signup for: {data.email}")

        response = supabase.auth.sign_up(
            {
                "email": data.email,
                "password": data.password
            }
        )

        print("Supabase signup response received")

        # Supabase should return a user after successful signup
        if response.user is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Unable to create user"
            )

        return {
            "message": "User created successfully",
            "user": {
                "id": str(response.user.id),
                "email": response.user.email,
                "created_at": response.user.created_at
            }
        }

    except HTTPException:
        raise

    except Exception as exc:
        # Print the REAL Supabase error in the terminal
        print("=" * 60)
        print("SUPABASE SIGNUP ERROR")
        print("Error type:", type(exc).__name__)
        print("Error:", str(exc))
        print("=" * 60)

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc)
        )


# ============================================================
# LOGIN
# ============================================================

@router.post("/auth/login")
def login(data: AuthRequest):
    """
    Log in an existing user using Supabase Auth.
    """

    # Validate required fields
    if not data.email or not data.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email and password are required"
        )

    try:
        response = supabase.auth.sign_in_with_password(
            {
                "email": data.email,
                "password": data.password
            }
        )

        if response.user is None or response.session is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid login credentials"
            )

        return {
            "message": "Login successful",
            "access_token": response.session.access_token,
            "refresh_token": response.session.refresh_token,
            "token_type": "bearer",
            "user": {
                "id": str(response.user.id),
                "email": response.user.email,
                "created_at": response.user.created_at
            }
        }

    except HTTPException:
        raise

    except Exception as exc:
        print("=" * 60)
        print("SUPABASE LOGIN ERROR")
        print("Error type:", type(exc).__name__)
        print("Error:", str(exc))
        print("=" * 60)

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid login credentials"
        )


# ============================================================
# LOGOUT
# ============================================================

@router.post("/auth/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(current_user=Depends(get_current_user)):
    """
    Log out the authenticated user.
    """

    try:
        supabase.auth.sign_out()
        return None

    except Exception as exc:
        print("Logout error:", str(exc))

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unable to logout"
        )


# ============================================================
# PUBLIC ROUTE
# ============================================================

@router.get("/public/info")
def public_info():
    """
    Public endpoint. No authentication required.
    """

    return {
        "message": "Welcome stranger! This info is public."
    }


# ============================================================
# PROTECTED PROFILE
# ============================================================

@router.get("/protected/profile")
def protected_profile(current_user=Depends(get_current_user)):
    """
    Protected endpoint.
    Requires a valid Supabase JWT.
    """

    return {
        "message": "You are authenticated!",
        "user": {
            "id": str(current_user.id),
            "email": current_user.email,
            "created_at": current_user.created_at
        }
    }


# ============================================================
# PROTECTED DASHBOARD
# ============================================================

@router.get("/protected/dashboard")
def protected_dashboard(current_user=Depends(get_current_user)):
    """
    Second protected endpoint.
    Uses the SAME authentication dependency.
    """

    return {
        "message": "Welcome to your protected dashboard!",
        "user": {
            "id": str(current_user.id),
            "email": current_user.email
        }
    }