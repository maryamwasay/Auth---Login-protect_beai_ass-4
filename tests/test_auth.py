from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == (
        "FlyRank A4 Authentication API is running"
    )


def test_public_info():
    response = client.get("/public/info")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == (
        "Welcome stranger! This info is public."
    )


def test_protected_profile_without_token():
    response = client.get("/protected/profile")

    assert response.status_code == 401

    data = response.json()

    assert data["detail"] == "Access token required"


def test_protected_dashboard_without_token():
    response = client.get("/protected/dashboard")

    assert response.status_code == 401


def test_admin_without_token():
    response = client.get("/protected/admin")

    assert response.status_code == 401
