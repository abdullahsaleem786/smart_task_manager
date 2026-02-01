from datetime import datetime


class FeatureBuilder:
    def __init__(self, task_service):
        self.task_service = task_service

    def _parse(self, iso_time):
        if not iso_time:
            return None
        return datetime.fromisoformat(iso_time)

    def build_features(self):
        tasks = self.task_service.list_tasks()
        features = []

        for t in tasks:
            if not t.get("completed") or not t.get("completed_at"):
                continue

            created = self._parse(t.get("created_at"))
            completed = self._parse(t.get("completed_at"))

            if not created or not completed:
                continue
            #Fix this
            duration = (completed - created).total_seconds() / 60

            features.append({
                "priority": t.get("priority", 3),
                "duration_minutes": round(duration, 2),
                "hour_created": created.hour,
                "day_of_week": created.weekday(),
                "completion_delay_minutes": round(duration, 2),
            })

        return features
