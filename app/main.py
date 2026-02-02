# app/main.py
from app.services.task_service import TaskService
from app.storage.json_store import JsonStore
from app.cli.menu import show_menu
from app.analytics.analytics_service import AnalyticsService
from app.ml.feature_builder import FeatureBuilder



def main():
    task_service = TaskService(JsonStore())
    analytics = AnalyticsService(task_service)
    feature_builder = FeatureBuilder(task_service)


    while True:
        show_menu()
        choice = input("Please Choose One Option: ")

        try:
            if choice == "1":
                title = input("Title: ")
                desc = input("Description: ")
                task_service.create_task(title, desc)

            elif choice == "2":
                for t in task_service.list_tasks():
                    status = "✓" if t["is_completed"] else "✗"
                    print(f"{t['id']} | [{status}] {t['title']}")

            elif choice == "3":
                task_id = input("Task ID: ").strip()
                task_service.complete_task(task_id)

            elif choice == "4":
                task_id = input("Task ID: ").strip()
                task_service.delete_task(task_id)

            elif choice == "5":
                summary = analytics.summary()
                for k, v in summary.items():
                    print(f"{k}: {v}")
                    
            elif choice == "6":
                trends = analytics.daily_summary()
                print("\nTasks Created Per Day:")
                for day, count in trends["created_per_day"].items():
                    print(f"{day}: {count}")

                print("\nTasks Completed Per Day:")
                for day, count in trends["completed_per_day"].items():
                    print(f"{day}: {count}")


            elif choice == "7":
                features = feature_builder.build_features()
                if not features:
                    print("No completed tasks available for ML features.")
                else:
                    print("ML-Ready Task Features:")
                    for f in features:
                        print(f)

            elif choice=='8':
                break

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
