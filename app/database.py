from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_KEY

# Create the Supabase client
supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)
