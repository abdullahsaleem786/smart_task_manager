from app.ml.task_duration_model import TaskDurationModel
from app.ml.feature_builder import build_features


def train():
    features = build_features()

    if len(features) < 5:
        print("Not enough data to train model.")
        return

    model = TaskDurationModel()
    model.train(features)
    print("Model trained and saved successfully.")


if __name__ == "__main__":
    train()
