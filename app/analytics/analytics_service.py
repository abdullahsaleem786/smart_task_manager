from datetime import datetime, timezone

class AnalyticsService:
    def __init__(self, task_service):
        self.task_service = task_service

    def _parse(self, value):
        if not value:
            return None
        return datetime.fromisoformat(value)

    def task_duration_minutes(self, task):
        created = self._parse(task.created_at)
        completed = self._parse(task.completed_at)

        if not created or not completed:
            return None

        if created.tzinfo is None:
            created = created.replace(tzinfo=timezone.utc)
        if completed.tzinfo is None:
            completed = completed.replace(tzinfo=timezone.utc)

        return (completed - created).total_seconds() / 60

    def summary(self):
        tasks = self.task_service.list_tasks()
        completed = [t for t in tasks if t.is_completed]

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
