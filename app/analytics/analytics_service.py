# app/analytics/analytics_service.py
from datetime import datetime


class AnalyticsService:
    def __init__(self, task_service):
        self.task_service = task_service

    def _parse_time(self, iso_time):
        return datetime.fromisoformat(iso_time)

    def task_duration_minutes(self, task):
        if not task["is_completed"]:
            return None

        if not task.get("completed_at"):
            return None

        created = self._parse_time(task["created_at"])
        completed = self._parse_time(task["completed_at"])
        return (completed - created).total_seconds() / 60

    def summary(self):
        tasks = self.task_service.list_tasks()

        total = len(tasks)
        completed = [t for t in tasks if t["is_completed"]]
        pending = total - len(completed)

        durations = [
            self.task_duration_minutes(t)
            for t in completed
            if self.task_duration_minutes(t) is not None
        ]

        avg_duration = (
            sum(durations) / len(durations) if durations else 0
        )

        return {
            "total_tasks": total,
            "completed_tasks": len(completed),
            "pending_tasks": pending,
            "average_completion_time_min": round(avg_duration, 2),
        }
