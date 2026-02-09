from app.cli.menu import show_menu
from app.cli.controller import CLIController
from app.services.task_service import TaskService
from app.storage.json_store import JsonStore
from app.analytics.analytics_service import AnalyticsService
from app.ml.feature_builder import FeatureBuilder


def main():
    storage = JsonStore()
    task_service = TaskService(storage)
    analytics = AnalyticsService(task_service)
    feature_builder = FeatureBuilder(task_service)

    controller = CLIController(
        task_service=task_service,
        analytics=analytics,
        feature_builder=feature_builder,
    )

    while True:
        show_menu()
        choice = input("Please Choose One Option: ").strip()
        controller.handle(choice)


if __name__ == "__main__":
    main()
