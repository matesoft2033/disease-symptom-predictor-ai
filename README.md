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

- data/                      Contains the Excel files (not included in repo)  
  - README.md                Instructions to get the dataset from Kaggle  

- src/  
  - data_preprocessing.py    Clean & prepare the dataset  
  - model.py                 Train and save ML model  
  - predict.py               Logic to turn symptoms → disease  
  - chatbot.py               Gives chatbot-style advice and tips  

- app/  
  - gradio_app.py            Main Gradio UI app  

- models/  
  - rf_model.pkl             Trained model file  

- notebooks/                 Jupyter notebooks for exploration  
  - 1_data_exploration.ipynb  
  - 2_preprocessing_test.ipynb  
  - 3_model_testing.ipynb  

- requirements.txt           Required Python packages  
- .gitignore  
- README.md                  You're here!

---

## 🧠 How It Works

1. User selects symptoms via checkboxes.  
2. The model receives a binary vector of symptoms.  
3. A trained classifier (Random Forest) predicts the most likely disease.  
4. The app returns:  
   - 🦠 Disease name  
   - 🧾 Description of related symptoms  
   - 🛡️ Suggested precautions  
   - 🤖 Encouragement from the chatbot  

---

## 📊 Dataset Source

This project uses the dataset from Kaggle:  
https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset

You must download the following files manually and place them in the `data/` folder:  
- `dataset.xlsx`  
- `symptom_description.xlsx`  
- `symptom_precaution.xlsx`  
- `symptom_severity.xlsx`  

---

## ⚙️ Installation

1. Clone the repo by running the following commands in your terminal:  
   git clone https://github.com/your-username/disease-symptom-prediction.git  
   cd disease-symptom-prediction  

2. Install the required Python packages by running:  
   pip install -r requirements.txt  

3. Run the app with this command:  
   python app/gradio_app.py  

4. Open your browser and go to http://127.0.0.1:7860 to use the application.  

---

## 🙌 Credits

- Dataset provided by [Itachi9604 on Kaggle](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset)  
- Machine learning model and preprocessing inspired by standard sklearn workflows  
- UI powered by [Gradio](https://gradio.app/)  
- Thanks to all open-source contributors  

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
