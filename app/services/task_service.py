from datetime import datetime
from app.models.task import Task


class TaskService:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load_tasks()

    def create_task(self, title, description="", priority=3):
        task = Task(title, description, priority)
        self.tasks.append(task.to_dict())
        self.storage.save_tasks(self.tasks)
        return task

    def list_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                task["completed_at"] = datetime.now().isoformat()
                self.storage.save_tasks(self.tasks)
                return True
        return False

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                self.tasks.pop(i)
                self.storage.save_tasks(self.tasks)
                return True
        return False
