import csv


class ExportService:
    def __init__(self, task_service):
        self.task_service = task_service

    def export_to_csv(self, file_path="data/tasks_dataset.csv"):
        tasks = self.task_service.list_tasks()

        if not tasks:
            raise ValueError("No tasks to export")

        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=tasks[0].keys())
            writer.writeheader()
            writer.writerows(tasks)

        return file_path
