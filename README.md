# FlyRank A4 — Authentication & Protected API

A secure FastAPI authentication API built for the **FlyRank Internship Backend Track — Week 2 — Assignment A4**.

This project uses **Supabase Auth** as the Identity Provider. Supabase handles user accounts, password hashing, authentication, and JWT issuance. The FastAPI backend verifies Supabase access tokens and protects authenticated routes using a reusable authentication dependency.

---

## Features

- User Sign Up
- User Login
- User Logout
- Supabase Authentication
- JWT access-token verification
- Protected API routes
- Reusable FastAPI authentication dependency
- Bearer token authentication
- Swagger UI documentation
- Public API endpoint
- Proper HTTP status codes
- Invalid/expired token rejection
- Environment-variable configuration
- Git-safe secret management

---

## Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Supabase Auth
- Supabase Python SDK
- Pydantic
- python-dotenv
- Swagger UI / OpenAPI
- Git & GitHub

---

## Project Structure

```text
flyrank-auth-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── auth.py
│   ├── dependencies.py
│   ├── models.py
│   └── routes.py
│
├── tests/
│   └── test_auth.py
│
├── ai-version/
│   └── README.md
│
├── screenshots/
│   ├── swagger.png
│   ├── signup.png
│   ├── login.png
│   ├── protected-success.png
│   └── invalid-token.png
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

> The `.env` file contains local configuration and must not be committed to GitHub.

---

# How Authentication Works

The authentication flow is:

```text
Client
   │
   │ email + password
   ▼
Supabase Auth
   │
   │ access token + refresh token
   ▼
Client
   │
   │ Authorization: Bearer <access_token>
   ▼
FastAPI
   │
   │ verify token
   ▼
Supabase
   │
   ├── Invalid token → 401
   │
   └── Valid token
          │
          ▼
    Protected Route
          │
          ▼
         200
```

The backend does **not** store passwords or implement password hashing.

Supabase manages user authentication and provides the JWT access token.

---

# Requirements

Make sure you have:

- Python 3.10 or newer
- Git
- A Supabase account
- A Supabase project

---

# 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd flyrank-auth-api
```

---

# 2. Create a Virtual Environment

Windows PowerShell:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

If the environment is activated, your terminal should show:

```text
(venv)
```

---

# 3. Install Dependencies

Run:

```powershell
pip install -r requirements.txt
```

---

# 4. Configure Supabase

Create a Supabase project.

In the Supabase Dashboard, find the project URL and publishable/anon key under the API settings.

Create a `.env` file in the project root:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_publishable_or_anon_key
PORT=8000
```

Example:

```env
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your_publishable_key
PORT=8000
```

### Important Security Rule

Never commit your real `.env` file to GitHub.

The repository contains `.env.example` instead:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_key
PORT=8000
```

The `.env` file is included in `.gitignore`.

---

# 5. Supabase Email Confirmation Setting

For this practice assignment, email confirmation can be disabled so that a newly registered account can log in immediately.

In Supabase:

```text
Authentication
    ↓
Sign In / Providers
    ↓
Email
    ↓
Confirm email
```

For production applications, email confirmation should normally remain enabled.

---

# 6. Start the Server

Run:

```powershell
uvicorn app.main:app --reload
```

The API will start at:

```text
http://127.0.0.1:8000
```

---

# 7. Swagger UI

FastAPI automatically provides Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger allows the API to be tested directly from the browser.

Protected endpoints use Bearer authentication.

Click:

```text
Authorize
```

and enter the access token received from the login endpoint.

---

# API Reference

| Method | Endpoint | Authentication | Description | Success |
|---|---|---|---|---|
| POST | `/auth/signup` | No | Create a new user | 201 |
| POST | `/auth/login` | No | Authenticate user and return JWT | 200 |
| POST | `/auth/logout` | Yes | Log out authenticated user | 204 |
| GET | `/public/info` | No | Public information | 200 |
| GET | `/protected/profile` | Yes | Return authenticated user's profile | 200 |
| GET | `/protected/dashboard` | Yes | Example protected dashboard | 200 |

---

# Authentication Status Codes

The API uses the following status codes:

| Status Code | Meaning |
|---|---|
| 200 | Successful request |
| 201 | User successfully created |
| 204 | Logout successful / no response body |
| 400 | Missing or invalid input |
| 401 | Missing, malformed, invalid, or expired token |
| 403 | Authenticated user is not authorized |
| 429 | Too many requests, when rate limiting is enabled |

---

# Endpoint Examples

## 1. Sign Up

### Request

```http
POST /auth/signup
```

JSON body:

```json
{
  "email": "test1@gmail.com",
  "password": "password123"
}
```

### Expected response

```text
201 Created
```

Example:

```json
{
  "message": "User created successfully",
  "user": {
    "id": "user-id",
    "email": "test1@gmail.com"
  }
}
```

---

# 2. Login

### Request

```http
POST /auth/login
```

JSON body:

```json
{
  "email": "test1@gmail.com",
  "password": "password123"
}
```

### Expected response

```text
200 OK
```

The response contains an access token and refresh token.

Example:

```json
{
  "message": "Login successful",
  "access_token": "YOUR_ACCESS_TOKEN",
  "refresh_token": "YOUR_REFRESH_TOKEN",
  "token_type": "bearer"
}
```

The `access_token` is used to access protected routes.

---

# 3. Public Information

### Request

```http
GET /public/info
```

No authentication is required.

### Response

```text
200 OK
```

Example:

```json
{
  "message": "Welcome stranger! This info is public."
}
```

---

# 4. Protected Profile

### Request

```http
GET /protected/profile
```

The request requires:

```http
Authorization: Bearer <ACCESS_TOKEN>
```

A valid token returns:

```text
200 OK
```

The endpoint returns authenticated user information such as:

- User ID
- Email
- Account creation date

---

# 5. Protected Profile Without Token

If the request does not contain an Authorization header:

```http
GET /protected/profile
```

the API returns:

```text
401 Unauthorized
```

Example:

```json
{
  "detail": "Access token required"
}
```

---

# 6. Invalid Token

If an invalid, modified, or expired token is provided:

```http
Authorization: Bearer invalid-token
```

the API returns:

```text
401 Unauthorized
```

Example:

```json
{
  "detail": "Invalid or expired token"
}
```

This prevents forged or tampered tokens from accessing protected resources.

---

# 7. Logout

### Request

```http
POST /auth/logout
```

Authentication is required.

The request must contain:

```http
Authorization: Bearer <ACCESS_TOKEN>
```

A successful logout returns:

```text
204 No Content
```

---

# 8. Protected Dashboard

### Request

```http
GET /protected/dashboard
```

This endpoint uses the same reusable authentication dependency as `/protected/profile`.

A valid token returns:

```text
200 OK
```

An invalid or missing token returns:

```text
401 Unauthorized
```

---

# JWT Verification

The protected routes do not simply trust the token supplied by the client.

The authentication dependency:

1. Reads the `Authorization` header.
2. Checks for the `Bearer` scheme.
3. Extracts the access token.
4. Sends the token to Supabase.
5. Supabase verifies the token.
6. Invalid or expired tokens are rejected.
7. Valid tokens allow the request to continue.
8. The authenticated user is made available to the protected route.

The reusable authentication dependency is implemented in:

```text
app/dependencies.py
```

Token verification is handled through:

```text
app/auth.py
```

---

# Reusable Authentication Dependency

FastAPI's dependency system is used as the authentication guard.

Protected routes use:

```python
Depends(get_current_user)
```

This prevents authentication logic from being duplicated across every protected endpoint.

For example:

```python
@router.get("/protected/profile")
def profile(user=Depends(get_current_user)):
    ...
```

Another protected route can use the same dependency:

```python
@router.get("/protected/dashboard")
def dashboard(user=Depends(get_current_user)):
    ...
```

---

# Swagger Authentication

Swagger UI provides an **Authorize** button for Bearer authentication.

The flow is:

```text
POST /auth/login
       ↓
Copy access_token
       ↓
Swagger → Authorize
       ↓
Paste token
       ↓
GET /protected/profile
       ↓
200 OK
```

The Swagger UI screenshot is included below.

## Swagger UI

![Swagger UI](screenshots/swagger.png)

---

# Testing

The authentication flow was tested using Swagger UI and curl.

## Test 1 — Signup

```bash
curl -i -X POST "http://127.0.0.1:8000/auth/signup" \
-H "Content-Type: application/json" \
-d "{\"email\":\"test1@gmail.com\",\"password\":\"password123\"}"
```

Expected:

```text
201 Created
```

---

## Test 2 — Login

```bash
curl -i -X POST "http://127.0.0.1:8000/auth/login" \
-H "Content-Type: application/json" \
-d "{\"email\":\"test1@gmail.com\",\"password\":\"password123\"}"
```

Expected:

```text
200 OK
```

The response contains:

```text
access_token
refresh_token
```

---

## Test 3 — Protected Route Without Token

```bash
curl -i "http://127.0.0.1:8000/protected/profile"
```

Expected:

```text
401 Unauthorized
```

---

## Test 4 — Protected Route With Valid Token

Replace `<ACCESS_TOKEN>` with the token received from login.

```bash
curl -i "http://127.0.0.1:8000/protected/profile" \
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

Expected:

```text
200 OK
```

---

## Test 5 — Tampered Token

Change one character in the access token and send it:

```bash
curl -i "http://127.0.0.1:8000/protected/profile" \
-H "Authorization: Bearer <TAMPERED_TOKEN>"
```

Expected:

```text
401 Unauthorized
```

This confirms that the backend verifies the token instead of simply trusting the client.

---

# Screenshots

The repository contains screenshots demonstrating the authentication flow.

```text
screenshots/
```

Examples include:

- Swagger UI
- Successful signup
- Successful login
- Protected route without authentication
- Protected route with a valid token
- Invalid/tampered token rejection
- Logout
- Protected dashboard

---

# Security

This project follows several important authentication security practices.

### Passwords are not stored by the API

The backend never stores user passwords.

Supabase Auth manages passwords and authentication.

### Tokens are verified

Protected routes do not trust JWTs without verification.

The token is checked through Supabase before allowing access.

### `.env` is ignored

Secrets are stored in:

```text
.env
```

and `.env` is included in `.gitignore`.

### No service-role key

The Supabase service-role/secret key must never be exposed in source code or committed to GitHub.

Only the appropriate public/publishable or anon key is used for this practice API.

---

# 401 vs 403

Authentication and authorization are different concepts.

### 401 Unauthorized

Means the API cannot establish a valid authenticated identity.

Examples:

- No token
- Malformed token
- Invalid token
- Expired token

Example:

```json
{
  "detail": "Invalid or expired token"
}
```

### 403 Forbidden

Means the API knows who the user is, but the user is not allowed to perform the requested action.

In simple terms:

```text
401 = I don't know you.

403 = I know who you are, but you are not allowed.
```

---

# Environment Variables

The project uses:

```text
SUPABASE_URL
SUPABASE_KEY
PORT
```

A template is provided in:

```text
.env.example
```

Example:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_key
PORT=8000
```

The real `.env` file is intentionally excluded from Git.

---

# Running the Project

After cloning the repository:

```powershell
python -m venv venv
```

Activate:

```powershell
venv\Scripts\activate
```

Install:

```powershell
pip install -r requirements.txt
```

Create `.env`:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_key
PORT=8000
```

Start:

```powershell
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

# AI Rematch — Stage 7

The optional AI rematch was completed in a separate directory:

```text
ai-version/
```

The purpose of this stage was to compare an AI-generated implementation with the manually developed authentication API.

The AI-generated version was kept separate from the main implementation.

The comparison focused on:

1. Authorization header and Bearer token extraction.
2. JWT verification.
3. Handling invalid or expired tokens.
4. Security issues such as trusting unverified tokens.
5. Secret handling.
6. Differences between the AI implementation and the manually developed implementation.

The AI version and comparison notes are documented in:

```text
ai-version/README.md
```

---

# Git Commit History

The assignment was developed in stages with separate commits.

The commit history follows the assignment stages:

```text
Stage 0: setup server and Supabase client
Stage 1: signup and login routes
Stage 2: public and protected routes
Stage 3: JWT token verification
Stage 4: authentication dependency and logout
Stage 5: Swagger bearer authentication
Stage 6: GitHub publication and README
Stage 7: AI rematch
```

---

# Assignment Checklist

| Requirement | Status |
|---|---|
| Supabase Auth configured | ✅ |
| Sign Up endpoint | ✅ |
| Login endpoint | ✅ |
| Logout endpoint | ✅ |
| Public endpoint | ✅ |
| Protected profile endpoint | ✅ |
| Protected dashboard endpoint | ✅ |
| JWT verification | ✅ |
| Reusable authentication dependency | ✅ |
| Bearer authentication | ✅ |
| Swagger UI | ✅ |
| Swagger Authorize button | ✅ |
| Missing token returns 401 | ✅ |
| Invalid token returns 401 | ✅ |
| Correct status codes | ✅ |
| `.env` configuration | ✅ |
| `.env` git-ignored | ✅ |
| `.env.example` included | ✅ |
| Screenshots included | ✅ |
| README documentation | ✅ |
| GitHub repository | ✅ |
| AI version | ✅ |

---

# Learning Outcomes

This assignment provided practical experience with:

- Authentication
- Authorization
- Supabase Auth
- JWTs
- Bearer tokens
- Authorization headers
- FastAPI dependencies
- Protected routes
- HTTP status codes
- Swagger/OpenAPI
- Environment variables
- API security
- Git and GitHub

The main security principle learned from this assignment is:

> Never trust credentials or tokens simply because the client sends them. Authentication data must be verified before protected resources are accessed.

---

# License

This project was created as part of the **FlyRank Internship — Backend Track — Week 2 — Assignment A4**.

See the `LICENSE` file for license information.
