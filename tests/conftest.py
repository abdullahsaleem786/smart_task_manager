import os
import pytest
from app.services.task_service import TaskService
from app.storage.json_store import JsonStore

TEST_FILE = "test_tasks.json"

@pytest.fixture
def task_service():
    # ensure clean state
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

    storage = JsonStore(TEST_FILE)
    service = TaskService(storage)
    yield service

    # cleanup
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
