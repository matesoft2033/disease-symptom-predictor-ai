import gradio as gr
import pickle
import numpy as np

# --- 1. Load Disease Prediction Model ---
with open("disease_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("symptoms.pkl", "rb") as f:
    all_symptoms = pickle.load(f)

# Preprocess symptoms
all_symptoms = sorted(all_symptoms)
display_symptoms = [s.replace('_', ' ').title() for s in all_symptoms]
label_to_symptom = dict(zip(display_symptoms, all_symptoms))

# --- 2. Medical Knowledge Base ---
MEDICAL_KNOWLEDGE = {

    "migraine": [
        "For migraines: (1) Rest in dark room (2) OTC pain relievers (ibuprofen/acetaminophen) (3) Apply cold compress (4) Consult neurologist if frequent",
        "Migraine treatment options include triptans (prescription) and caffeine. Avoid triggers like bright lights or strong smells."
    ],

    "allergy": [
        "Allergy management: (1) Antihistamines (cetirizine/loratadine) (2) Nasal sprays (3) Allergy shots (immunotherapy) for severe cases",
        "For food allergies: Strict avoidance, carry epinephrine auto-injector (EpiPen), read food labels carefully"
    ],
    "cold": [
        "Treat colds with rest, fluids, and OTC pain relievers. See doctor if fever lasts >3 days",
        "Most colds resolve in 7-10 days. Use decongestants for nasal congestion"
    ],
    "headache": [
        "For headaches: Hydrate, rest, and use OTC pain relievers sparingly",
        "Persistent headaches require medical evaluation - consult your doctor"
    ],
    "fever": [
        "For fever: Rest, fluids, and acetaminophen/ibuprofen. Seek help if >39°C or lasts >3 days",
        "High fever warning: Seek emergency care if fever >40°C or with stiff neck"
    ]
}

SPECIAL_RESPONSES = {
    "general approaches": "I can provide specific guidance for: allergies, migraines, colds, fever, back pain, rashes. What condition are you asking about?",
    "consult a doctor": "For these symptoms, seek medical care: severe pain, difficulty breathing, sudden weakness, high fever (>103°F), or symptoms lasting >7 days"
}

def get_medical_response(user_query):
    user_query = user_query.lower()

    # First check for special cases
    for phrase, response in SPECIAL_RESPONSES.items():
        if phrase in user_query:
            return response

    # Then check medical conditions
    for condition, responses in MEDICAL_KNOWLEDGE.items():
        if condition in user_query:
            return np.random.choice(responses)

    # Final improvement - suggest related conditions
    related = [cond for cond in MEDICAL_KNOWLEDGE.keys() if cond in user_query]
    if related:
        return f"Are you asking about {', '.join(related)}? {np.random.choice(MEDICAL_KNOWLEDGE[related[0]])}"

    return "I can advise on: " + ", ".join(MEDICAL_KNOWLEDGE.keys()) + ". Please be more specific."

# --- 3. Disease Prediction Function ---
def predict_disease(selected_labels):
    if not selected_labels or len(selected_labels) < 4:
        return "⚠️ Please select at least 4 symptoms for accurate results."

    user_symptoms = [label_to_symptom[label] for label in selected_labels]
    input_vector = [1 if symptom in user_symptoms else 0 for symptom in all_symptoms]
    input_vector = np.array([input_vector])
    probas = model.predict_proba(input_vector)[0]
    max_proba = np.max(probas)
    predicted = model.classes_[np.argmax(probas)]

    sorted_indices = np.argsort(probas)[::-1]
    top_diseases = [
        f"<b>{i+1}. {model.classes_[idx]}</b> — {probas[idx]*100:.1f}%"
        for i, idx in enumerate(sorted_indices[:3])
    ]

    prediction_result = (
        f"<div style='background: #001a33; padding: 15px; border-radius: 8px; margin-bottom: 15px;'>"
        f"<h3 style='color: #4fc3f7; margin-top: 0;'>🩺 Predicted Disease</h3>"
        f"<p style='font-size: 18px; color: white;'>{predicted} <span style='color: #4fc3f7'>({max_proba*100:.1f}% confidence)</span></p>"
        "</div>"
        "<div style='background: #001a33; padding: 15px; border-radius: 8px;'>"
        "<h3 style='color: #4fc3f7; margin-top: 0;'>🔍 Top 3 Possible Diseases</h3>"
        "<ul style='color: white; padding-left: 20px;'>" +
        "".join([f"<li>{d}</li>" for d in top_diseases]) +
        "</ul>"
        "</div>"
    )
    return prediction_result

# --- 4. Chat Responder ---
def chatbot_respond(message, chat_history):
    response = get_medical_response(message)
    return chat_history + [(message, response)], ""

# --- 5. UI Setup ---
custom_css = """
:root {
    --primary: #4fc3f7;
    --secondary: #001a33;
    --text: #ffffff;
    --bg: #0a192f;
    --card-bg: #0a2342;
    --error: #ff6b6b;
}
body, .gradio-container {
    background: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Segoe UI', Roboto, sans-serif;
}
/* [Keep all your existing CSS styles] */
"""

with gr.Blocks(css=custom_css) as demo:
    gr.Markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h1 style="margin-bottom: 5px;">🧬 Medical Diagnosis Assistant</h1>
        <p style="color: #4fc3f7; font-size: 16px;">Select symptoms for diagnosis and get medical advice</p>
    </div>
    """)

    with gr.Row(equal_height=True):
        with gr.Column(scale=1, min_width=300):
            gr.Markdown("### 🔍 Symptom Checker")
            symptoms_input = gr.CheckboxGroup(
                choices=display_symptoms,
                label="Select your symptoms:",
                interactive=True
            )
            predict_btn = gr.Button("Analyze Symptoms", variant="primary")
            prediction_output = gr.Markdown(
                label="Diagnosis Results",
                value="Your results will appear here..."
            )

        with gr.Column(scale=1, min_width=400):
            gr.Markdown("### 💬 Medical Advisor")
            chatbot = gr.Chatbot(
                label="Chat with Medical Advisor",
                show_label=False,
                bubble_full_width=False
            )
            with gr.Row():
                user_input = gr.Textbox(
                    placeholder="Ask about symptoms or treatments...",
                    label="",
                    show_label=False,
                    container=False,
                    scale=7
                )
                send_btn = gr.Button("Send", scale=1, min_width=80)

    # Event handlers
    predict_btn.click(
        fn=predict_disease,
        inputs=symptoms_input,
        outputs=prediction_output
    )
    send_btn.click(
        fn=chatbot_respond,
        inputs=[user_input, chatbot],
        outputs=[chatbot, user_input]
    )
    user_input.submit(
        fn=chatbot_respond,
        inputs=[user_input, chatbot],
        outputs=[chatbot, user_input]
    )

demo.launch()
