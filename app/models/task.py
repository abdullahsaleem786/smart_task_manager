# app/models/task.py
from datetime import datetime
from uuid import uuid4


class Task:
    def __init__(self, title: str, description: str = "", priority: int = 3):
        self.id = str(uuid4())
        self.title = title
        self.description = description
        self.priority = priority
        self.created_at = datetime.utcnow().isoformat()
        self.completed_at = None
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True
        self.completed_at = datetime.utcnow().isoformat()

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data: dict):
        task = Task(
            title=data["title"],
            description=data.get("description", ""),
            priority=data.get("priority", 3),
        )
        task.__dict__.update(data)
        return task
