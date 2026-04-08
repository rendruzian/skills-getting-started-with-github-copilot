def test_get_activities_returns_dictionary(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert expected_activity in payload


def test_get_activities_contains_participants_list(client):
    # Arrange
    activity_name = "Programming Class"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert "participants" in payload[activity_name]
    assert isinstance(payload[activity_name]["participants"], list)
