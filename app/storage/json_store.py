import json
from pathlib import Path
from app.models.task import Task

class JsonStore:
    def __init__(self, path: str = "tasks.json"):
        self.path = Path(path)

    def load(self) -> list[Task]:
        if not self.path.exists():
            return []

        raw = json.loads(self.path.read_text())
        return [Task.from_dict(t) for t in raw]

    def save(self, tasks: list[Task]) -> None:
        self.path.write_text(
            json.dumps([t.to_dict() for t in tasks], indent=2)
        )
