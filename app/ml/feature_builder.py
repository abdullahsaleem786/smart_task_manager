# app/ml/feature_builder.py
from datetime import datetime


class FeatureBuilder:
    def __init__(self, task_service):
        self.task_service = task_service

    def _parse(self, iso_time):
        return datetime.fromisoformat(iso_time)

    def build_features(self):
        tasks = self.task_service.list_tasks()
        features = []

        for t in tasks:
            if not t.get("completed") or not t.get("completed_at"):
                continue

            created = self._parse(t["created_at"])
            completed = self._parse(t["completed_at"])

            duration = (completed - created).total_seconds() / 60

            features.append({
                "priority": t["priority"],
                "hour_created": created.hour,
                "day_of_week": created.weekday(),
                "description_length": len(t.get("description", "")),
                "duration_minutes": round(duration, 2),
            })

        return features
