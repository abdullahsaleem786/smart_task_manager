import pandas as pd
from sklearn.linear_model import LinearRegression
from joblib import dump, load
import os


class TaskDurationModel:
    def __init__(self, model_path="task_duration_model.joblib"):
        self.model_path = model_path
        self.model = None

    def train(self, features):
        if len(features) < 3:
            raise ValueError("Not enough data to train model")

        df = pd.DataFrame(features)

        X = df[["priority", "hour_created", "day_of_week", "description_length"]]
        y = df["duration_minutes"]

        self.model = LinearRegression()
        self.model.fit(X, y)

        dump(self.model, self.model_path)

    def load(self):
        if not os.path.exists(self.model_path):
            raise FileNotFoundError("Model not trained yet")
        self.model = load(self.model_path)

    def predict(self, feature):
        if self.model is None:
            self.load()

        df = pd.DataFrame([feature])
        return float(self.model.predict(df)[0])
