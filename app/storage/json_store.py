import json
import os


class JsonStore:
    def __init__(self, file_path="tasks.json"):
        self.file_path = file_path

    def load(self):
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r") as f:
            return json.load(f)

    def save(self, tasks):
        with open(self.file_path, "w") as f:
            json.dump(tasks, f, indent=2)
