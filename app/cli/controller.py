from app.services.task_service import TaskService
from app.analytics.analytics_service import AnalyticsService
from app.services.export_service import ExportService

class Controller:
    def __init__(self, task_service, analytics):
        self.task_service = task_service
        self.analytics = analytics
        self.export_service = ExportService(self.task_service)

    def filter_tasks(self):
        print("\n1. Completed Tasks")
        print("2. Pending Tasks")
        option = input("Choose filter: ")

        if option == "1":
            tasks = self.task_service.completed_tasks()
        elif option == "2":
            tasks = self.task_service.pending_tasks()
        else:
            print("Invalid filter")
            return

        if not tasks:
            print("No tasks found.")
            return

        for t in tasks:
            print(f"{t.id} - {t.title}")

    def handle(self, choice: str):
        if choice == "1":
            title = input("Task title: ")
            self.task_service.create_task(title)
        elif choice == "2":
            for t in self.task_service.list_tasks():
                print(t.id, "-", t.title)

        elif choice == "3":
            task_id = input("Task ID to complete: ")
            if not self.task_service.complete_task(task_id):
                print("Task not found")

        elif choice == "4":
            task_id = input("Task ID to delete: ")
            if not self.task_service.delete_task(task_id):
                print("Task not found")

        elif choice == "5":
            summary = self.analytics.summary()
            print(summary)
        elif choice == "6":
            self.filter_tasks()
        elif choice == "7":
            success = self.export_service.export_tasks_to_csv()
            if success:
                print("Tasks exported to tasks_export.csv")
            else:
                print("No tasks to export")

