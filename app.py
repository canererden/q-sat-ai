from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# ========== 1️⃣ MODELLERİ YÜKLE ==========
MODEL_DIR = "trained_models"
models = {}

for f in os.listdir(MODEL_DIR):
    if f.endswith(".pkl"):
        model_path = os.path.join(MODEL_DIR, f)
        model_name = f.replace(".pkl", "")
        models[model_name] = joblib.load(model_path)
        print(f"✅ Model yüklendi: {model_name}")

print(f"Toplam {len(models)} model yüklendi.")


# ========== 2️⃣ ÖZELLİKLER ==========
NUMERIC_FEATURES = [
    'Research Scope',
    'Researcher Competence',
    'Knowledge Power',
    'Interview Count',
    'Interview Duration',
    'Observation Duration',
    'Homogeneity/Heterogeneity',
    'Participant Originality',
    'Data Variety',
    'Data Quality'
]

feature_info = {
    "Research Scope": {
        "label": "Research Scope",
        "tooltip": "Broader scope requires more participants; narrow scope requires fewer.",
        "options": [("10", "Narrow (10)"), ("15", "Medium (15)"), ("20", "Broad (20)")]
    },
    "Researcher Competence": {
        "label": "Researcher Competence",
        "tooltip": "Experienced researchers need fewer participants.",
        "options": [("10", "Small (10)"), ("15", "Medium (15)"), ("20", "Large (20)")]
    },
    "Knowledge Power": {
        "label": "Information Power",
        "tooltip": "High participant expertise reduces sample size.",
        "options": [("10", "Expert (10)"), ("15", "Medium (15)"), ("20", "not expert (20)")]
    },
    "Interview Count": {
        "label": "Number of Interviews",
        "tooltip": "More interviews per participant reduce sample size.",
        "options": [("10", "More than 10 (10)"), ("15", "More than 5 (15)"),("20", "Less than 5 (20)")]
    },
    "Interview Duration": {
        "label": "Interview Duration",
        "tooltip": "Longer interviews yield more data per participant.",
        "options": [("10", "More than 2 hours (10)"), ("20", "Less than 1 hour (20)")]
    },
    "Observation Duration": {
        "label": "Observation Duration",
        "tooltip": "Longer observation periods reduce sample size.",
        "options": [("10", "Long (10)"), ("15", "Medium (15)"), ("20", "Short (20)")]
    },
    "Homogeneity/Heterogeneity": {
        "label": "Sample Homogeneity",
        "tooltip": "Homogeneous groups require fewer participants.",
        "options": [("10", "Homogeneous (10)"),("15", "Medium (15)"), ("20", "Heterogeneous (20)")]
    },
    "Participant Originality": {
        "label": "Participant Originality",
        "tooltip": "Unique participants provide richer data, reducing sample size.",
        "options": [("10", "High (10)"),("15", "Medium (15)"), ("20", "Low (20)")]
    },
    "Data Variety": {
        "label": "Data Diversity (Triangulation)",
        "tooltip": "Multiple data sources reduce the need for a large sample.",
        "options": [("10", "High (10)"), ("15", "Medium (15)"), ("20", "Low (20)")]
    },
    "Data Quality": {
        "label": "Data Quality",
        "tooltip": "High-quality data reduces sample size.",
        "options": [("10", "High (10)"), ("15", "Medium (15)"), ("20", "Low (20)")]
    }
}

RESEARCH_DESIGN_OPTIONS = [
    'Case Study',
    'Ethnographic Research',
    'Grounded Theory',
    'Narrative Research',
    'Phenomenology'
]

OHE_FEATURES = [
    'Research Design_Case Study',
    'Research Design_Ethnographic Research',
    'Research Design_Grounded Theory',
    'Research Design_Narrative Research',
    'Research Design_Phenomenology'
]

TRAIN_FEATURES = NUMERIC_FEATURES + OHE_FEATURES


# ========== 3️⃣ ARAYÜZ ==========
@app.route("/", methods=["GET", "POST"])
def index():
    prediction_results = None

    if request.method == "POST":
        try:
            # --- 1. Sayısal girdileri al ---
            user_input = {f: float(request.form.get(f, 0)) for f in NUMERIC_FEATURES}

            # --- 2. Research Design seçimini al ---
            selected_design = request.form.get("Research Design")

            # --- 3. One-hot encoding oluştur ---
            for d in RESEARCH_DESIGN_OPTIONS:
                col_name = f"Research Design_{d}"
                user_input[col_name] = 1.0 if d == selected_design else 0.0

            # --- 4. DataFrame oluştur ---
            df_new = pd.DataFrame([user_input])[TRAIN_FEATURES]

            # --- 5. Tahmin yap ---
            predictions = {}
            for name, model in models.items():
                y_pred_log = model.predict(df_new)
                y_pred = np.expm1(y_pred_log)  # log dönüşümünü geri al
                predictions[name] = round(float(y_pred[0]), 2)

            # --- 6. Ensemble ortalama ---
            ensemble_mean = round(np.mean(list(predictions.values())), 2)

            prediction_results = {
                "input": user_input,
                "predictions": predictions,
                "ensemble_mean": ensemble_mean
            }

        except Exception as e:
            prediction_results = {"error": str(e)}

    return render_template(
    "index.html",
    results=prediction_results,
    numeric_features=NUMERIC_FEATURES,
    research_designs=RESEARCH_DESIGN_OPTIONS,
    feature_info=feature_info)

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html')

# ========== 4️⃣ FLASK SUNUCUSU ==========
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
