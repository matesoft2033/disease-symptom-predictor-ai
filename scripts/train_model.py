from src.data_preprocessing import load_and_clean_data, get_all_symptoms, vectorize_symptoms
from src.model import train_model, evaluate_model
from sklearn.model_selection import train_test_split

df = load_and_clean_data("data/dataset.csv")
all_symptoms, symptom_cols = get_all_symptoms(df)
df_vectorized = vectorize_symptoms(df, all_symptoms, symptom_cols)

X = df_vectorized.drop("disease", axis=1)
y = df_vectorized["disease"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)

model = train_model(X_train, y_train)
evaluate_model(model, X_train, y_train, label="Train")
evaluate_model(model, X_test, y_test, label="Test")

