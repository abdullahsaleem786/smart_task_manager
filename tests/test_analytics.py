from app.services.task_service import TaskService
from app.analytics.analytics_service import AnalyticsService
from app.storage.json_store import JsonStore
import os

TEST_FILE = "test_analytics.json"

def setup_function():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_summary_counts():
    storage = JsonStore(TEST_FILE)
    service = TaskService(storage)
    analytics = AnalyticsService(service)

    t1 = service.create_task("Task 1")
    t2 = service.create_task("Task 2")
    service.complete_task(t1.id)

    summary = analytics.summary()

    assert summary["total_tasks"] == 2
    assert summary["completed_tasks"] == 1
    assert summary["pending_tasks"] == 1
