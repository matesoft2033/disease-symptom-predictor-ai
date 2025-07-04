from src.predict import load_model, predict_disease, print_top_diseases
from src.data_preprocessing import load_and_clean_data, get_all_symptoms

model = load_model()
df = load_and_clean_data("data/dataset.csv")
all_symptoms, _ = get_all_symptoms(df)

user_symptoms = ['nausea', 'vomiting', 'abdominal_pain', 'diarrhoea']

predicted, probas = predict_disease(model, user_symptoms, all_symptoms)
print_top_diseases(probas, model, top_n=5)
