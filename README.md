# Auth---Login-protect_beai_ass-4
# FastAPI Supabase Authentication System

## Project Overview

This project implements a secure authentication system using **FastAPI** and **Supabase Authentication**.

The application provides user registration, login, JWT-based authentication, protected routes, and logout functionality.

The purpose of this assignment is to demonstrate how to integrate Supabase Auth with a FastAPI backend and secure API endpoints using Bearer JWT tokens.

---

# Features

## Authentication Features

✅ User Registration  
- Create a new user account using email and password.
- User credentials are managed through Supabase Authentication.

✅ User Login  
- Authenticate users using Supabase Auth.
- Generate JWT access tokens after successful login.

✅ JWT Authentication  
- Protect API routes using JWT Bearer authentication.
- Validate user tokens before allowing access to protected resources.

✅ Protected Routes  
- Only authenticated users can access protected endpoints.

✅ Logout  
- Invalidate user session.
- Verify that old tokens cannot access protected routes after logout.

---

# Technologies Used

- Python
- FastAPI
- Supabase Authentication
- JWT (JSON Web Tokens)
- Uvicorn
- Pydantic
- Swagger UI for API testing

---

# Project Structure
