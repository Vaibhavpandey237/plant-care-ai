"""
tests/test_auth_pages.py — Unit & Integration tests for Authentication, About Us, and Contact Us.
"""

import pytest
from app import create_app
from database import repository


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SECRET_KEY"] = "test-key"
    with app.test_client() as client:
        yield client


def test_signup_login_logout_flow(client):
    # 1. Sign Up
    signup_res = client.post(
        "/signup",
        data={
            "username": "gardener1",
            "email": "gardener1@example.com",
            "password": "password123",
            "confirm_password": "password123",
        },
        follow_redirects=True,
    )
    assert signup_res.status_code == 200

    user = repository.get_user_by_email("gardener1@example.com")
    assert user is not None
    assert user["username"] == "gardener1"

    # 2. Logout
    logout_res = client.get("/logout", follow_redirects=True)
    assert logout_res.status_code == 200

    # 3. Login
    login_res = client.post(
        "/login",
        data={
            "email_or_username": "gardener1@example.com",
            "password": "password123",
        },
        follow_redirects=True,
    )
    assert login_res.status_code == 200


def test_about_and_contact_pages(client):
    about_res = client.get("/about")
    assert about_res.status_code == 200
    assert b"About Plant Care AI" in about_res.data

    contact_res = client.get("/contact")
    assert contact_res.status_code == 200
    assert b"Contact Us" in contact_res.data

    # Contact form post
    post_res = client.post(
        "/contact",
        data={
            "name": "Jane Grower",
            "email": "jane@grower.org",
            "subject": "Plant Care Advice",
            "message": "Need help with tomato leaf spots.",
        },
        follow_redirects=True,
    )
    assert post_res.status_code == 200
    assert b"Thank you for reaching out!" in post_res.data
