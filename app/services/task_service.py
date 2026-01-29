# app/services/task_service.py
from app.models.task import Task


class TaskService:
    def __init__(self, store):
        self.store = store

    def create_task(self, title, description="", priority=3):
        task = Task(title, description, priority)
        tasks = self.store.get_all()
        tasks.append(task.to_dict())
        self.store.save_all(tasks)
        return task

    def list_tasks(self):
        return self.store.get_all()

    def complete_task(self, task_id):
        tasks = self.store.get_all()
        for t in tasks:
            if t["id"] == task_id:
                t["is_completed"] = True
                return self.store.save_all(tasks)
        raise ValueError("Task not found")

    def delete_task(self, task_id):
        tasks = self.store.get_all()
        new_tasks = [t for t in tasks if t["id"] != task_id]
        if len(tasks) == len(new_tasks):
            raise ValueError("Task not found")
        self.store.save_all(new_tasks)
