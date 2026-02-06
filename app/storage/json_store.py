# app/storage/json_store.py

import json
import os


class JsonStore:
    def __init__(self, file_path="data/tasks.json"):
        self.file_path = file_path
        self._ensure_file_exists()

    # ---------- Internal Helpers ----------

    def _ensure_file_exists(self):
        directory = os.path.dirname(self.file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)

    # ---------- Public API (LOCKED) ----------

    def load(self):
        """Load all tasks from JSON."""
        with open(self.file_path, "r") as f:
            return json.load(f)

    def save(self, tasks):
        """Persist all tasks to JSON."""
        with open(self.file_path, "w") as f:
            json.dump(tasks, f, indent=2)
