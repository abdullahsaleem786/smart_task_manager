from typing import List
from app.models.task import Task
from app.storage.base import BaseStore


class TaskService:
    def __init__(self, storage: BaseStore):
        self.storage = storage
        self._tasks: List[Task] = self.storage.load()

    def _save(self):
        self.storage.save(self._tasks)

    def _find(self, task_id: int) -> Task | None:
        return next((t for t in self._tasks if t.id == task_id), None)

    def create_task(self, title: str, priority: int):
        task_id = max((t.id for t in self._tasks), default=0) + 1
        self._tasks.append(Task(task_id, title, priority=priority))
        self._save()

    def list_tasks(self) -> List[Task]:
        return self._tasks

    def list_tasks_by_priority(self, priority: int) -> List[Task]:
        return [t for t in self._tasks if t.priority == priority]

    def complete_task(self, task_id: int) -> bool:
        task = self._find(task_id)
        if not task:
            return False
        task.complete()
        self._save()
        return True

    def delete_task(self, task_id: int) -> bool:
        task = self._find(task_id)
        if not task:
            return False
        self._tasks.remove(task)
        self._save()
        return True
    def completed_tasks(self):
        return [t for t in self._tasks if t.is_completed]

    def pending_tasks(self):
        return [t for t in self._tasks if not t.is_completed]

