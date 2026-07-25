# Auth---Login-protect_beai_ass-4
# FastAPI Supabase Authentication System

## Project Description

This project is a backend authentication system built using **FastAPI** and **Supabase Authentication**.

The application implements a complete authentication workflow including:

- User registration
- User login
- JWT access token generation
- Protected API routes
- Token validation
- User logout
- Authentication testing using Swagger UI

The main purpose of this assignment is to integrate **Supabase Auth with FastAPI** and secure backend APIs using **JWT Bearer Authentication**.

---

# Features

## 1. User Registration

Users can create a new account using their email and password.

The registration process is handled through Supabase Authentication.

**Endpoint:**

```
POST /auth/register
```

---

## 2. User Login

Registered users can log in using their credentials.

After successful authentication, Supabase generates a JWT access token.

**Endpoint:**

```
POST /auth/login
```

Example response:

```json
{
    "access_token": "JWT_TOKEN",
    "token_type": "bearer"
}
```

---

## 3. JWT Authentication

The application uses JWT Bearer tokens to authenticate users.

Protected routes require a valid access token in the request header.

Example:

```
Authorization: Bearer <access_token>
```

---

## 4. Protected Dashboard

Only authenticated users can access protected resources.

**Endpoint:**

```
GET /protected/dashboard
```

Successful response:

```json
{
    "message": "Welcome test126@gmail.com",
    "dashboard": "This is a protected dashboard."
}
```

---

## 5. Logout Functionality

Users can log out from the system.

After logout, the previous access token becomes invalid and cannot access protected routes.

**Endpoint:**

```
POST /auth/logout
```

Successful response:

```
204 No Content
```

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | Backend Framework |
| Supabase Auth | User Authentication |
| JWT | Secure Token Authentication |
| Uvicorn | ASGI Server |
| Pydantic | Data Validation |
| Swagger UI | API Testing |

---

# Project Structure

```
FastAPI-Supabase-Auth/

│
├── main.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
└── app/
    │
    ├── routers/
    │   │
    │   ├── auth.py
    │   └── protected.py
    │
    ├── services/
    │   │
    │   └── supabase.py
    │
    ├── dependencies/
    │   │
    │   └── auth.py
    │
    └── config.py
```

---

# Installation and Setup

## Step 1: Clone Repository

```bash
git clone <your-github-repository-url>
```

Navigate into the project:

```bash
cd FastAPI-Supabase-Auth
```

---

## Step 2: Create Virtual Environment

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate the environment.

### Windows:

```bash
venv\Scripts\activate
```

### Linux/Mac:

```bash
source venv/bin/activate
```

---

## Step 3: Install Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

---

# Environment Configuration

Create a `.env` file in the project root.

Example:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_key
```

### Important:

Do not upload `.env` file to GitHub because it contains sensitive information.

The project includes:

```
.env.example
```

which contains only the required variable names.

---

# Running the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The application will run at:

```
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically provides Swagger documentation.

Open:

```
http://127.0.0.1:8000/docs
```

Swagger UI allows testing all API endpoints.

---

# API Endpoints

## Authentication APIs

---

## Register User

### Request

```
POST /auth/register
```

Purpose:

Creates a new user account.

---

## Login User

### Request

```
POST /auth/login
```

Purpose:

Authenticates user and returns JWT access token.

---

## Logout User

### Request

```
POST /auth/logout
```

Purpose:

Logs out the user and invalidates the session.

Response:

```
204 No Content
```

---

# Protected APIs

## Dashboard

### Request

```
GET /protected/dashboard
```

Authentication:

Requires JWT Bearer Token.

Example:

```
Authorization: Bearer <token>
```

---

# Authentication Workflow

```
User Registration
        |
        |
        v
Supabase Creates Account
        |
        |
        v
User Login
        |
        |
        v
JWT Access Token Generated
        |
        |
        v
Token Added To Request Header
        |
        |
        v
Protected Routes Accessible
        |
        |
        v
Logout
        |
        |
        v
Old Token Rejected
```

---

# Testing Results

All API endpoints were tested successfully.

## Test Summary

| Test Case | Status |
|-----------|--------|
| Server Running | ✅ Passed |
| User Registration | ✅ Passed |
| User Login | ✅ Passed |
| Access Token Generation | ✅ Passed |
| Swagger Authorization | ✅ Passed |
| Protected Dashboard Access | ✅ Passed |
| Logout Endpoint | ✅ Passed |
| Old Token After Logout | ✅ Rejected |
| New Token After Login | ✅ Passed |

---

# Example Testing Results

## Successful Protected Route Access

Request:

```
GET /protected/dashboard
```

Response:

```json
{
    "message": "Welcome test126@gmail.com",
    "dashboard": "This is a protected dashboard."
}
```

---

## Logout Test

Request:

```
POST /auth/logout
```

Response:

```
204 No Content
```

---

## Invalid Token Test

After logout, using the old token:

Response:

```json
{
    "detail": "Invalid or expired token"
}
```

Status:

```
401 Unauthorized
```

---

# Security Implementation

The project follows these security practices:

- JWT-based authentication
- Protected API endpoints
- Environment variable management
- Secret keys excluded from repository
- Token validation before accessing resources
- Unauthorized access prevention

---

# Future Improvements

Possible improvements:

- Add user profile management
- Add refresh token support
- Add role-based authorization
- Add database integration
- Add automated unit tests

---

# Assignment Completion

This assignment has been successfully completed.

Implemented:

✅ FastAPI Backend  
✅ Supabase Authentication  
✅ User Registration  
✅ User Login  
✅ JWT Authentication  
✅ Protected Routes  
✅ Logout Functionality  
✅ API Testing  

---

# Author

**Your Name**
