import os
import sys
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# add project root to python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from backend.utils.preprocessing import load_and_preprocess


def train_model():

    # load processed dataset
    X_train, X_test, y_train, y_test, encoder = load_and_preprocess()

    print("Training model...")

    # create model
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    # train model
    model.fit(X_train, y_train)

    print("Model trained successfully")

    # predictions
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print("Model Accuracy:", accuracy)

    # save model
    base_dir = os.path.dirname(os.path.dirname(__file__))

    model_path = os.path.join(base_dir, "model_weights", "disease_model.pkl")

    joblib.dump(model, model_path)

    print("Model saved at:", model_path)


if __name__ == "__main__":
    train_model()