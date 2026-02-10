import json
from pathlib import Path
from app.models.task import Task

class JsonStore:
    def __init__(self, file_path: str = "tasks.json"):
        self.path = Path(file_path)

    def load(self) -> list[Task]:
        if not self.path.exists():
            return []

        with open(self.path, "r", encoding="utf-8") as f:
            raw = json.load(f)

        return [Task.from_dict(t) for t in raw]

    def save(self, tasks: list[Task]):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in tasks], f, indent=2)
