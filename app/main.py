# app/main.py
from app.services.task_service import TaskService
from app.storage.json_store import JsonStore
from app.cli.menu import show_menu
from app.analytics.analytics_service import AnalyticsService
from app.ml.feature_builder import FeatureBuilder
from app.services.task_service import TaskService
from app.storage.json_store import JsonStore
from app.ml.feature_builder import FeatureBuilder
from app.ml.evaluator import evaluate



def main():
    task_service = TaskService(JsonStore())


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
            elif choice == "8":
                from datetime import datetime
                from app.ml.task_duration_model import TaskDurationModel

                title = input("Title: ")
                description = input("Description: ")
                priority = int(input("Priority (1-5): "))

                feature = {
                        "priority": priority,
                        "hour_created": datetime.now().hour,
                        "day_of_week": datetime.now().weekday(),
                        "description_length": len(description),
                        }

                features = feature_builder.build_features()

                if len(features) < 3:
                    print("Not enough completed tasks to train ML model.")
                    return

                model = TaskDurationModel()
                model.train(features)

                predicted = model.predict(feature)
                print(f"Estimated completion time: {round(predicted, 2)} minutes")
            elif choice == "9":
                from app.ml.evaluator import evaluate
                from app.ml.feature_builder import FeatureBuilder
                from app.storage.json_store import JsonStore
                from app.services.task_service import TaskService
                from app.ml.evaluator import evaluate

                task_service = TaskService(JsonStore())
                feature_builder = FeatureBuilder(task_service)

                features = feature_builder.build_features()

                if len(features) < 5:
                    print("Not enough data for evaluation.")
                    return

                baseline_mae, ml_mae = evaluate(features)

                print(f"Baseline MAE: {round(baseline_mae, 2)} minutes")
                print(f"ML Model MAE: {round(ml_mae, 2)} minutes")

                if ml_mae < baseline_mae:
                    print("✅ ML model beats baseline.")
                else:
                    print("❌ ML model does NOT beat baseline.")


            elif choice=='10':
                break

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
