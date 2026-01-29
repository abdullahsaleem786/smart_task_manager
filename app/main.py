# app/main.py
from app.services.task_service import TaskService
from app.storage.json_store import JsonStore
from app.cli.menu import show_menu


def main():
    service = TaskService(JsonStore())

    while True:
        show_menu()
        choice = input("Choose: ")

        try:
            if choice == "1":
                title = input("Title: ")
                desc = input("Description: ")
                service.create_task(title, desc)

            elif choice == "2":
                for t in service.list_tasks():
                    status = "✓" if t["is_completed"] else "✗"
                    print(f"{t['id']} | [{status}] {t['title']}")

            elif choice == "3":
                task_id = input("Task ID: ")
                service.complete_task(task_id)

            elif choice == "4":
                task_id = input("Task ID: ")
                service.delete_task(task_id)

            elif choice == "5":
                break

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
