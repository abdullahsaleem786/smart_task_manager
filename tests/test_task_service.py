from app.services.task_service import TaskService
from app.storage.json_store import JsonStore
import os

TEST_FILE = "test_tasks.json"

def setup_function():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_create_task():
    storage = JsonStore(TEST_FILE)
    service = TaskService(storage)

    task = service.create_task("Test Task")

    assert task.title == "Test Task"
    assert task.is_completed is False

def test_complete_task():
    storage = JsonStore(TEST_FILE)
    service = TaskService(storage)

    task = service.create_task("Complete Me")
    result = service.complete_task(task.id)

    assert result is True
    assert task.is_completed is True

def test_list_tasks_returns_task_objects(task_service):
    tasks = task_service.list_tasks()
    assert all(hasattr(t, "id") for t in tasks)

