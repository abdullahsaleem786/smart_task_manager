# app/services/task_service.py

from datetime import datetime
from app.models.task import Task


class TaskService:
    def __init__(self, storage):
        self.storage = storage
        self._tasks = self.storage.load()  # single load point

    # ---------- Internal Helpers ----------

    def _save(self):
        """Persist current in-memory state."""
        self.storage.save(self._tasks)

    def _find_task(self, task_id):
        for task in self._tasks:
            if task["id"] == task_id:
                return task
        return None

    # ---------- Public API ----------

    def create_task(self, title, description="", priority=3):
        task = Task(title, description, priority)
        self._tasks.append(task.to_dict())
        self._save()
        return task.to_dict()

    def list_tasks(self):
        return list(self._tasks)  # defensive copy

    def complete_task(self, task_id):
        task = self._find_task(task_id)
        if not task:
            raise ValueError("Task not found")

        if task["is_completed"]:
            raise ValueError("Task already completed")

        task["is_completed"] = True
        task["completed_at"] = datetime.now().isoformat()
        self._save()

    def delete_task(self, task_id):
        task = self._find_task(task_id)
        if not task:
            raise ValueError("Task not found")

        self._tasks.remove(task)
        self._save()
