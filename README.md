# 🧠 Disease Symptom Prediction AI

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/github/license/matesoft2033/disease-symptom-prediction)
![Issues](https://img.shields.io/github/issues/mateosft2033/disease-symptom-prediction)

AI-powered tool that predicts possible diseases based on symptoms using a trained machine learning model and provides chatbot-style suggestions.

---

## 📁 Project Structure

```
disease-symptom-prediction/
├── data/               # Excel dataset (not uploaded)
│   └── README.md       # Instructions for downloading from Kaggle
│
├── src/                # Source code
│   ├── data_preprocessing.py   # Cleans & prepares dataset
│   ├── model.py                # Trains and saves the ML model
│   ├── predict.py              # Predicts disease from symptoms
│   └── chatbot.py              # Symptom-checker chatbot logic
│
├── app/                # App interface
│   └── gradio_app.py   # Gradio-based web UI
│
├── models/             # Trained model files
│   └── rf_model.pkl
│
├── notebooks/          # Jupyter notebooks for analysis
│   ├── 1_data_exploration.ipynb
│   ├── 2_preprocessing_test.ipynb
│   └── 3_model_testing.ipynb
│
├── requirements.txt    # Python dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/disease-symptom-prediction.git
cd disease-symptom-prediction
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the App

```bash
python app/gradio_app.py
```

The app will start locally and you can open it in your browser at `http://localhost:7860`.

---

## 🤖 Features

- ✅ Predict disease from symptoms
- 🧠 Trained on structured healthcare dataset
- 💬 Chatbot-style health advice
- 🖥️ User-friendly Gradio interface

---

<details>
<summary>📦 Dataset Note (Click to expand)</summary>

We use a healthcare dataset available on [Kaggle](https://www.kaggle.com/). Due to licensing, it is not uploaded in this repo. Please download it manually and place it in the `data/` directory.

</details>

---

## 🪪 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Credits

Created by [Mate](https://github.com/your-username) — feel free to fork, star, or contribute.

---
