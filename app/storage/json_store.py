import json
import os
from app.models.task import Task

class JsonStore:
    def __init__(self, path: str):
        self.path = path

    def load(self) -> list[Task]:
        if not os.path.exists(self.path):
            return []  # 🔥 CRITICAL FIX

        with open(self.path, "r", encoding="utf-8") as f:
            raw = json.load(f)

        return [Task.from_dict(d) for d in raw]

    def save(self, tasks: list[Task]):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in tasks], f, indent=2)
