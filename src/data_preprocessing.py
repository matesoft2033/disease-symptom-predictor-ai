import pandas as pd
import numpy as np

def load_and_clean_data(path):
    df = pd.read_csv(path)
    df.sort_values(by='Disease', inplace=True)
    df.drop_duplicates(inplace=True)
    df.fillna("none", inplace=True)
    df.columns = df.columns.str.strip().str.lower()
    for col in df.columns:
        df[col] = df[col].astype(str).str.strip().str.lower()
    return df

def get_all_symptoms(df):
    symptom_cols = [col for col in df.columns if col.startswith('symptom')]
    all_symptoms = set()
    for col in symptom_cols:
        for val in df[col].unique():
            if val != 'none':
                all_symptoms.add(val)
    return sorted(all_symptoms), symptom_cols

def vectorize_symptoms(df, all_symptoms, symptom_cols):
    df_num = pd.DataFrame(df['disease'])
    for symptom in all_symptoms:
        df_num[symptom] = df[symptom_cols].apply(lambda row: int(symptom in row.values), axis=1)
    return df_num

