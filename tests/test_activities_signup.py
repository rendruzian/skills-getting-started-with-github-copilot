import pytest

import src.app as app_module


def test_signup_adds_participant(client):
    # Arrange
    activity_name = "Chess Club"
    email = "new.student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity_name}"
    assert email in app_module.activities[activity_name]["participants"]


def test_signup_returns_404_for_unknown_activity(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_returns_400_for_duplicate_participant(client):
    # Arrange
    activity_name = "Chess Club"
    existing_email = app_module.activities[activity_name]["participants"][0]

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup", params={"email": existing_email}
    )

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"


@pytest.mark.xfail(strict=True, reason="Capacity validation is not implemented yet")
def test_signup_rejects_when_activity_is_full(client):
    # Arrange
    activity_name = "Capacity Test Club"
    app_module.activities[activity_name] = {
        "description": "Temporary full activity for test",
        "schedule": "Fridays, 4:00 PM - 5:00 PM",
        "max_participants": 1,
        "participants": ["filled@mergington.edu"],
    }

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup", params={"email": "second@mergington.edu"}
    )

    # Assert
    assert response.status_code == 400


@pytest.mark.xfail(strict=True, reason="Email validation is not implemented yet")
def test_signup_rejects_empty_email(client):
    # Arrange
    activity_name = "Chess Club"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": ""})

    # Assert
    assert response.status_code == 422
