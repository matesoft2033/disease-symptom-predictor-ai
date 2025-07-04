from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import joblib

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, 'models/rf_model.pkl')
    return model

def evaluate_model(model, X, y, label="Set"):
    y_pred = model.predict(X)
    acc = accuracy_score(y, y_pred)
    f1 = f1_score(y, y_pred, average="weighted")
    print(f"{label} Accuracy: {acc:.4f}")
    print(f"{label} F1 Score: {f1:.4f}")

