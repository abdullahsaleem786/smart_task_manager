import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from app.ml.task_duration_model import TaskDurationModel


def evaluate(features):
    df = pd.DataFrame(features)

    X = df[["priority", "hour_created", "day_of_week", "description_length"]]
    y = df["duration_minutes"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Baseline
    baseline_pred = [y_train.mean()] * len(y_test)
    baseline_mae = mean_absolute_error(y_test, baseline_pred)

    # ML Model
    model = TaskDurationModel()
    model.model.fit(X_train, y_train)
    ml_pred = model.model.predict(X_test)
    ml_mae = mean_absolute_error(y_test, ml_pred)

    return baseline_mae, ml_mae
