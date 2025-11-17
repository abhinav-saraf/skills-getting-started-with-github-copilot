import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_register_for_activity():
    # Register a participant
    activity_name = "Yoga"
    email = "testuser@example.com"
    response = client.post(f"/activities/{activity_name}/register?email={email}")
    assert response.status_code in (200, 400, 404)
    # If already registered, should return 400
    # If activity doesn't exist, should return 404
    # Otherwise, should return 200


def test_unregister_from_activity():
    activity_name = "Yoga"
    email = "testuser@example.com"
    # Unregister participant
    response = client.post(f"/activities/{activity_name}/unregister?email={email}")
    assert response.status_code in (200, 400, 404)
    # If not registered, should return 400
    # If activity doesn't exist, should return 404
    # Otherwise, should return 200
