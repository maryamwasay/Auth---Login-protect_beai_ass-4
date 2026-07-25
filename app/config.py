from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()

# Read environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
PORT = os.getenv("PORT")
