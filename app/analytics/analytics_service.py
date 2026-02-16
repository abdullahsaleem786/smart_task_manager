from datetime import datetime, timezone
from app.models.task import Task


class AnalyticsService:
    def __init__(self, task_service):
        self.task_service = task_service

    def _parse(self, value: str | None):
        if not value:
            return None
        dt = datetime.fromisoformat(value)
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)

    def task_duration_minutes(self, task: Task):
        created = self._parse(task.created_at)
        completed = self._parse(task.completed_at)

        if not created or not completed:
            return None

        return (completed - created).total_seconds() / 60

    def summary(self):
        tasks = self.task_service.list_tasks()

        completed = [t for t in tasks if t.completed_at]

        durations = [
            self.task_duration_minutes(t)
            for t in completed
            if self.task_duration_minutes(t) is not None
        ]

        avg = round(sum(durations) / len(durations), 2) if durations else 0

        return {
            "total_tasks": len(tasks),
            "completed_tasks": len(completed),
            "pending_tasks": len(tasks) - len(completed),
            "average_completion_time_min": avg,
            }
