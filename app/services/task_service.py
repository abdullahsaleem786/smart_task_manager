from datetime import datetime
from app.models.task import Task

class TaskService:
    def __init__(self, storage):
        self.storage = storage
        self._tasks = self.storage.load()

    def _save(self):
        self.storage.save(self._tasks)

    def create_task(self, title, description="", priority=3):
        task = Task(title, description, priority).to_dict()
        self._tasks.append(task)
        self._save()
        return task

    def list_tasks(self):
        return self._tasks

    def _find_task(self, task_id):
        return next((t for t in self._tasks if t["id"] == task_id), None)

    def complete_task(self, task_id):
        task = self._find_task(task_id)
        if not task:
            return False

        task["is_completed"] = True
        task["completed_at"] = datetime.now().isoformat()
        self._save()
        return True

    def delete_task(self, task_id):
        before = len(self._tasks)
        self._tasks = [t for t in self._tasks if t["id"] != task_id]
        if len(self._tasks) == before:
            return False
        self._save()
        return True
