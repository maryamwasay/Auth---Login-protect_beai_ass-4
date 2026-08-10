from fastapi import FastAPI

from .routes import router


app = FastAPI(
    title="FlyRank A4 - Authentication API",
    description=(
        "Secure authentication API using FastAPI and Supabase Auth. "
        "Includes signup, login, logout, JWT verification, "
        "protected routes, refresh tokens, and Swagger bearer authentication."
    ),
    version="1.0.0",
)


app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "FlyRank A4 Authentication API is running",
        "docs": "/docs",
        "public": "/public/info",
    }