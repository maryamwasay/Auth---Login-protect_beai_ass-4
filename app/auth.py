import os

from dotenv import load_dotenv
from supabase import create_client, Client


# Load environment variables from .env
load_dotenv()


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


# Check required environment variables
if not SUPABASE_URL:
    raise RuntimeError(
        "SUPABASE_URL is missing. Check your .env file."
    )

if not SUPABASE_KEY:
    raise RuntimeError(
        "SUPABASE_KEY is missing. Check your .env file."
    )


# Clean accidental spaces or quotes
SUPABASE_URL = SUPABASE_URL.strip().strip('"').strip("'")
SUPABASE_KEY = SUPABASE_KEY.strip().strip('"').strip("'")


# Startup diagnostics
print("=" * 60)
print("Supabase configuration")
print("SUPABASE_URL:", SUPABASE_URL)
print("SUPABASE_KEY loaded:", bool(SUPABASE_KEY))
print("=" * 60)


# Create Supabase client
supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


# ============================================================
# VERIFY SUPABASE ACCESS TOKEN
# ============================================================

def get_user_from_token(token: str):
    """
    Verify a Supabase access token and return the authenticated user.

    Supabase verifies the JWT for us.
    """

    if not token:
        raise ValueError("Access token required")

    response = supabase.auth.get_user(token)

    if response is None or response.user is None:
        raise ValueError("Invalid or expired token")

    return response.user