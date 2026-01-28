# app/main.py
from app.services.task_service import TaskService
from app.storage.json_store import JsonStore


def main():
    service = TaskService(JsonStore())

    while True:
        print("\n1. Add Task")
        print("2. List Tasks")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            task = service.create_task(title, desc)
            print(f"Task created: {task.title}")

        elif choice == "2":
            tasks = service.list_tasks()
            for t in tasks:
                status = "✓" if t["is_completed"] else "✗"
                print(f"[{status}] {t['title']}")

        elif choice == "3":
            break


if __name__ == "__main__":
    main()
