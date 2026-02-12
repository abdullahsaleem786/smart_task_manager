import json
from pathlib import Path
from typing import List
from app.models.task import Task
from app.storage.base import BaseStore


class JsonStore(BaseStore):
    def __init__(self, file_path: str = "tasks.json"):
        self.path = Path(file_path)

    def load(self) -> List[Task]:
        if not self.path.exists():
            return []

        with open(self.path, "r", encoding="utf-8") as f:
            raw = json.load(f)

        return [Task.from_dict(t) for t in raw]

    def save(self, tasks: List[Task]) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in tasks], f, indent=2)
