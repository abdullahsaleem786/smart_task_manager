from app.exceptions import TaskNotFoundError
from datetime import datetime
from datetime import datetime, timezone

# Ensure the "current" time is also offset-aware
now = datetime.now(timezone.utc)

class CLIController:
    def __init__(self, task_service, analytics, feature_builder):
        self.task_service = task_service
        self.analytics = analytics
        self.feature_builder = feature_builder

    def handle(self, choice):
        try:
            match choice:
                case "1":
                    self.add_task()
                case "2":
                    self.list_tasks()
                case "3":
                    self.complete_task()
                case "4":
                    self.delete_task()
                case "5":
                    self.view_analytics()
                case "6":
                    self.view_daily_trends()
                case "7":
                    self.view_ml_features()
                case "8":
                    self.predict_duration()
                case "9":
                    self.evaluate_model()
                case "10":
                    print("Exiting Smart Task Manager.")
                    raise SystemExit
                case _:
                    print("Invalid option.")
        except TaskNotFoundError as e:
            print(e)
        except ValueError as e:
            print(e)

    def add_task(self):
        title = input("Title: ")
        desc = input("Description: ")
        self.task_service.create_task(title, desc)

    def list_tasks(self):
        for t in self.task_service.list_tasks():
            status = "✓" if t["is_completed"] else "✗"
            print(f"{t['id']} | [{status}] {t['title']}")

    def complete_task(self):
        task_id = input("Task ID: ").strip()
        self.task_service.complete_task(task_id)

    def delete_task(self):
        task_id = input("Task ID: ").strip()
        self.task_service.delete_task(task_id)

    def view_analytics(self):
        summary = self.analytics.summary()
        for k, v in summary.items():
            print(f"{k}: {v}")

    def view_daily_trends(self):
        trends = self.analytics.daily_summary()
        print("\nTasks Created Per Day:")
        for day, count in trends["created_per_day"].items():
            print(f"{day}: {count}")

        print("\nTasks Completed Per Day:")
        for day, count in trends["completed_per_day"].items():
            print(f"{day}: {count}")

    def view_ml_features(self):
        features = self.feature_builder.build_features()
        if not features:
            print("No completed tasks available.")
            return
        for f in features:
            print(f)

    def predict_duration(self):
        from app.ml.task_duration_model import TaskDurationModel

        title = input("Title: ")
        desc = input("Description: ")
        priority = int(input("Priority (1–5): "))

        feature = {
            "priority": priority,
            "hour_created": datetime.now(timezone.utc).hour,
            "day_of_week": datetime.now(timezone.utc).weekday(),
            "description_length": len(desc),
        }

        features = self.feature_builder.build_features()
        if len(features) < 3:
            print("Not enough data.")
            return

        model = TaskDurationModel()
        model.train(features)
        prediction = model.predict(feature)

        print(f"Estimated completion time: {round(prediction, 2)} minutes")

    def evaluate_model(self):
        from app.ml.evaluator import evaluate

        features = self.feature_builder.build_features()
        if len(features) < 5:
            print("Not enough data for evaluation.")
            return

        baseline, ml = evaluate(features)
        print(f"Baseline MAE: {round(baseline, 2)}")
        print(f"ML MAE: {round(ml, 2)}")
