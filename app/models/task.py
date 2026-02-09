from datetime import datetime, timezone,UTC
import uuid

class Task:
    def __init__(self, title, description="", priority=3):
        self.id = ...
        self.title = title
        self.description = description
        self.priority = priority
        self.is_completed = False
        self.created_at = datetime.utcnow().isoformat()
        self.completed_at = None

    def complete(self):
        self.is_completed = True
        self.completed_at = datetime.now(timezone.utc).isoformat()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "created_at": self.created_at,
            "completed_at": self.completed_at,
            "is_completed": self.is_completed,
        }

    @staticmethod
    def from_dict(data: dict) -> "Task":
        return Task(
            title=data["title"],
            description=data.get("description", ""),
            priority=data.get("priority", 3),
            task_id=data["id"],
            created_at=data.get("created_at"),
            completed_at=data.get("completed_at"),
            is_completed=data.get("is_completed", False),
        )
