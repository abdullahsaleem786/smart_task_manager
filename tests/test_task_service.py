from app.services.task_service import TaskService
from app.storage.json_store import JsonStore
import os
class InMemoryStore:
    def __init__(self):
        self._tasks = []

    def load(self):
        return list(self._tasks)

    def save(self, tasks):
        self._tasks = list(tasks)



def setup_test_service():
    test_file = "data/test_tasks.json"
    if os.path.exists(test_file):
        os.remove(test_file)
    return TaskService(JsonStore(test_file))


def test_create_task():
    service = setup_test_service()
    task = service.create_task("Test Task")

    assert task["title"] == "Test Task"
    assert task["is_completed"] is False


def test_complete_task():
    service = setup_test_service()
    task = service.create_task("Complete Me")

    service.complete_task(task["id"])
    tasks = service.list_tasks()

    assert tasks[0]["is_completed"] is True


def test_delete_task():
    service = setup_test_service()
    task = service.create_task("Delete Me")

    service.delete_task(task["id"])
    assert len(service.list_tasks()) == 0
def test_complete_nonexistent_task():
    service = TaskService(InMemoryStore())

    result = service.complete_task("non-existent-id")

    assert result is False

