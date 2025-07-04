import numpy as np
import joblib

def load_model(path='models/rf_model.pkl'):
    return joblib.load(path)

def predict_disease(model, user_symptoms, all_symptoms, threshold=0.5):
    input_vector = [1 if symptom in user_symptoms else 0 for symptom in all_symptoms]
    input_vector = np.array([input_vector])
    probas = model.predict_proba(input_vector)
    predicted = model.classes_[np.argmax(probas)]
    max_proba = np.max(probas)

    if max_proba < threshold:
        print("⚠️ Warning: Model not confident.")
    print(f"Predicted: {predicted} (Confidence: {max_proba*100:.1f}%)")
    return predicted, probas

def print_top_diseases(probas, model, top_n=3):
    sorted_indices = np.argsort(probas[0])[::-1]
    classes = model.classes_
    print(f"\nTop {top_n} predictions:")
    for i in range(min(top_n, len(classes))):
        print(f"{i+1}. {classes[sorted_indices[i]]}: {probas[0][sorted_indices[i]]:.4f}")

