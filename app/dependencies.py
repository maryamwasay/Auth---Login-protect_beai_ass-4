from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from .auth import get_user_from_token


# Swagger / FastAPI Bearer authentication
security = HTTPBearer(
    auto_error=False
)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """
    Reusable authentication dependency.

    It:
    1. Checks whether Authorization: Bearer <token> exists.
    2. Extracts the JWT.
    3. Sends the JWT to Supabase for verification.
    4. Returns the authenticated user.
    """

    # No Authorization header
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Access token required"
        )

    # Make sure it is a Bearer token
    if credentials.scheme.lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Access token required"
        )

    token = credentials.credentials

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Access token required"
        )

    try:
        user = get_user_from_token(token)
        return user

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )