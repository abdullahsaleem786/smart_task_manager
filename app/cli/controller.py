from app.services.task_service import TaskService
from app.analytics.analytics_service import AnalyticsService

class Controller:
    def __init__(self, task_service, analytics):
        self.task_service = task_service
        self.analytics = analytics

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
