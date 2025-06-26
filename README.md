# 🧠 Disease Symptom Prediction App

An AI-powered web application that predicts possible diseases based on user-selected symptoms and gives friendly health advice — like a chatbot.

---

## 🚀 Features

- ✅ Select symptoms from a list (checkbox UI)  
- ✅ Predict the most likely disease using a trained machine learning model  
- ✅ Get helpful, friendly chatbot-style messages with:  
  - 🛡️ Health precautions  
  - 📖 Symptom descriptions  
  - 💬 Encouragement & self-care tips  

---

## 📂 Project Structure

disease-symptom-prediction/  
├── data/                      # Excel files (download manually from Kaggle)  
│   └── README.md              # Instructions for dataset placement  
├── src/                       # Core logic  
│   ├── data_preprocessing.py  # Clean & prepare the dataset  
│   ├── model.py               # Train and save ML model  
│   ├── predict.py             # Predict disease from symptoms  
│   └── chatbot.py             # Generate chatbot-style advice  
├── app/  
│   └── gradio_app.py          # Gradio UI web app  
├── models/  
│   └── rf_model.pkl           # Trained Random Forest model  
├── notebooks/                 # Jupyter notebooks for exploration  
│   ├── 1_data_exploration.ipynb  
│   ├── 2_preprocessing_test.ipynb  
│   └── 3_model_testing.ipynb  
├── requirements.txt           # Python package dependencies  
├── .gitignore                 # Files to ignore in Git  
└── README.md                  # Project documentation (this file)

---

## 🧠 How It Works

1. User selects symptoms via checkboxes  
2. A binary vector is created based on selected symptoms  
3. Random Forest classifier predicts the most likely disease  
4. The app displays:  
   - 🦠 Disease name  
   - 📖 Description of symptoms  
   - 🛡️ Suggested precautions  
   - 💬 Friendly chatbot advice  

---

## 📊 Dataset Source

This project uses the dataset from Kaggle:  
https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset

Place these files in the `data/` folder after downloading:  
- `dataset.xlsx`  
- `symptom_description.xlsx`  
- `symptom_precaution.xlsx`  
- `symptom_severity.xlsx`  

---

## ⚙️ Installation

1. Clone the repository:  
   `git clone https://github.com/your-username/disease-symptom-prediction.git`  
   `cd disease-symptom-prediction`

2. Install the required packages:  
   `pip install -r requirements.txt`

3. Run the app:  
   `python app/gradio_app.py`

4. Open your browser and go to:  
   `http://127.0.0.1:7860`

---

## 🙌 Credits

- Dataset by [Itachi9604 on Kaggle](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset)  
- UI powered by [Gradio](https://gradio.app/)  
- Machine learning model built with Scikit-learn  
- Thanks to all open-source contributors  

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
