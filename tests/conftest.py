from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module

ORIGINAL_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities() -> None:
    app_module.activities.clear()
    app_module.activities.update(deepcopy(ORIGINAL_ACTIVITIES))


@pytest.fixture
def client() -> TestClient:
    return TestClient(app_module.app)
