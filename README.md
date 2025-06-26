# 🧠 Disease Symptom Prediction App

An AI-powered web application that predicts possible diseases based on user-selected symptoms and gives friendly health advice — like a chatbot.

---

## 🚀 Features

* ✅ Select symptoms from a list (checkbox UI)
* ✅ Predict the most likely disease using a trained machine learning model
* ✅ Get helpful, friendly chatbot-style messages with:

  * 🛡️ Health precautions
  * 📖 Symptom descriptions
  * 💬 Encouragement & self-care tips

---

## 📂 Project Structure

```
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
```

---

## 🧠 How It Works

1. User selects symptoms via checkboxes
2. A binary vector is created based on selected symptoms
3. Random Forest classifier predicts the most likely disease
4. The app displays:

   * 🦠 Disease name
   * 📖 Description of symptoms
   * 🛡️ Suggested precautions
   * 💬 Friendly chatbot advice

---

## 📊 Dataset Source

This project uses the dataset from Kaggle:
[https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset)

Place all `.csv` files from the dataset in the `/data` folder.

---

## ⚙️ Installation

1. **Clone the repo:**

```bash
git clone https://github.com/your-username/disease-symptom-prediction.git
cd disease-symptom-prediction
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the app:**

```bash
cd app
python gradio_app.py
```

---

## ✍️ Credits

Created by \[Mate].
Thanks to the open-source community for datasets and libraries.

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` file for details.
