from fastapi import Header, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.database import supabase

# Create Bearer Authentication Scheme
security = HTTPBearer()


def verify_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    try:

        response = supabase.auth.get_user(token)

        return response.user

    except Exception:

        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )
