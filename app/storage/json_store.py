# app/storage/json_store.py
import json
from pathlib import Path


class JsonStore:
    def __init__(self, file_path=Path("data/tasks.json")):
        self.file_path = file_path
        self.file_path.parent.mkdir(exist_ok=True)

        if not self.file_path.exists():
            self._write([])

    def _read(self):
        with open(self.file_path, "r") as f:
            return json.load(f)

    def _write(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def get_all(self):
        return self._read()

    def save_all(self, tasks):
        self._write(tasks)
