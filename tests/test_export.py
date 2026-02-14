from app.services.task_service import TaskService
from app.services.export_service import ExportService
from app.storage.json_store import JsonStore
import os

TEST_FILE = "test_export.json"
CSV_FILE = "tasks_export.csv"

def setup_function():
    for f in [TEST_FILE, CSV_FILE]:
        if os.path.exists(f):
            os.remove(f)

def test_export_csv():
    storage = JsonStore(TEST_FILE)
    service = TaskService(storage)
    exporter = ExportService(service)

    service.create_task("Export Me")

    result = exporter.export_tasks_to_csv(CSV_FILE)

    assert result is True
    assert os.path.exists(CSV_FILE)
