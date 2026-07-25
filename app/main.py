from fastapi import FastAPI

from app.routers.auth import router as auth_router
from app.routers.public import router as public_router
from app.routers.protected import router as protected_router

app = FastAPI(
    title="Supabase Authentication API",
    description="Authentication API using FastAPI and Supabase",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Supabase Authentication API is running!"
    }


app.include_router(auth_router)
app.include_router(public_router)
app.include_router(protected_router)
