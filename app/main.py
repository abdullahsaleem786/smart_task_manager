from app.storage.json_store import JsonStore
from app.services.task_service import TaskService
from app.analytics.analytics_service import AnalyticsService
from app.cli.controller import Controller
from app.services.task_service import TaskService
from app.analytics.analytics_service import AnalyticsService


def main():
    storage = JsonStore()
    task_service = TaskService(storage)
    analytics = AnalyticsService(task_service)
    controller = Controller(task_service, analytics)

    while True:
        print("\n1. Create Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. View Analytics")
        print("0. Exit")

        choice = input("Please Choose One Option: ")
        if choice == "0":
            break

        controller.handle(choice)

if __name__ == "__main__":
    main()
