import csv
from pathlib import Path

class ExportService:
    def __init__(self, task_service):
        self.task_service = task_service

    def export_tasks_to_csv(self, filename="tasks_export.csv"):
        tasks = self.task_service.list_tasks()

        if not tasks:
            return False

        path = Path(filename)

        with open(path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # header
            writer.writerow([
                "id",
                "title",
                "is_completed",
                "created_at",
                "completed_at"
            ])

            for task in tasks:
                writer.writerow([
                    task.id,
                    task.title,
                    task.is_completed,
                    task.created_at,
                    task.completed_at
                ])

        return True
