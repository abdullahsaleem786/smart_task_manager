# app/services/task_service.py
from app.models.task import Task
from app.storage.json_store import JsonStore


class TaskService:
    def __init__(self, store: JsonStore):
        self.store = store

    def create_task(self, title, description="", priority=3):
        task = Task(title, description, priority)
        self.store.save_task(task)
        return task

    def list_tasks(self):
        return self.store.load_tasks()
