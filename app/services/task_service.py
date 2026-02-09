from datetime import datetime
from app.models.task import Task
from app.exceptions import TaskNotFoundError


class TaskService:
    def __init__(self, storage):
        self.storage = storage
        self._tasks = self.storage.load()

    def _save(self):
        self.storage.save(self._tasks)

    def _find_task(self, task_id):
        return next((t for t in self._tasks if t["id"] == task_id), None)

    def create_task(self, title, description="", priority=3):
        task = Task(title, description, priority)
        self._tasks.append(task.to_dict())
        self._save()
        return task.to_dict()

    def list_tasks(self):
        return self._tasks

    def complete_task(self, task_id):
        task = self._find_task(task_id)
        if not task:
            raise TaskNotFoundError("Task not found")

        task["is_completed"] = True
        task["completed_at"] = datetime.now().isoformat()
        self._save()

    def delete_task(self, task_id):
        task = self._find_task(task_id)
        if not task:
            raise TaskNotFoundError("Task not found")

        self._tasks.remove(task)
        self._save()
