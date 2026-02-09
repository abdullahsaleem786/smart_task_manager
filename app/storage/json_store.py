import json
from pathlib import Path


class JsonStore:
    def __init__(self, file_path="tasks.json"):
        self.file = Path(file_path)

    def load(self):
        if not self.file.exists():
            return []
        return json.loads(self.file.read_text())

    def save(self, tasks):
        self.file.write_text(json.dumps(tasks, indent=2))
