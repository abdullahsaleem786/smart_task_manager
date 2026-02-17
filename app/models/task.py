from datetime import datetime, timezone
import uuid
#Ready this code for Day-20
class Task:
    def __init__(
        self,
        title: str,
        priority: str = "medium",
        description: str = "",
        task_id: str | None = None,
        created_at: str | None = None,
        completed_at: str | None = None,
        is_completed: bool = False,
    ):
        self.id = task_id or str(uuid.uuid4())
        self.title = title
        self.description = description
        self.priority = priority
        self.created_at = created_at or datetime.now(timezone.utc).isoformat()
        self.completed_at = completed_at
        self.is_completed = is_completed


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
            task_id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            priority=data.get("priority", 3),
            created_at=data.get("created_at"),
            completed_at=data.get("completed_at"),
            is_completed=data.get("is_completed", False),
        )
