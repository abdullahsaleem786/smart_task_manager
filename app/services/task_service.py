from app.models.task import Task
from app.storage.json_store import JsonStore

class TaskService:
    def __init__(self, storage: JsonStore):
        self.storage = storage
        self._tasks: list[Task] = self.storage.load()

    def _save(self):
        self.storage.save(self._tasks)

    def create_task(self, title, description="", priority=3) -> Task:
        task = Task(title, description, priority)
        self._tasks.append(task)
        self._save()
        return task

    def list_tasks(self) -> list[Task]:
        return self._tasks

    def _find_task(self, task_id: str) -> Task | None:
        return next((t for t in self._tasks if t.id == task_id), None)

    def complete_task(self, task_id: str) -> bool:
        task = self._find_task(task_id)
        if not task:
            return False

        task.complete()
        self._save()
        return True

    def delete_task(self, task_id: str) -> bool:
        task = self._find_task(task_id)
        if not task:
            return False

        self._tasks.remove(task)
        self._save()
        return True
