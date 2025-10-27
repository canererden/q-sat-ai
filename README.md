<p align="center">
  <img src="static/logo.svg" alt="Q-Sat AI Logo" width="50%">
</p>

<h1 align="center">Q-Sat AI</h1>
<h3 align="center">Machine Learning-Based Decision Support for Data Saturation in Qualitative Studies</h3>

<p align="center">
  <a href="https://q-sat-ai.up.railway.app/" target="_blank">
    <img src="https://img.shields.io/badge/Live_Demo-Railway_App-brightgreen?style=for-the-badge&logo=railway" alt="Railway Live Demo">
  </a>
  <a href="https://q-sat-ai.onrender.com/" target="_blank">
    <img src="https://img.shields.io/badge/Live_Demo-Render_App-brightgreen?style=for-the-badge&logo=render" alt="Render Live Demo">
  </a>
  <a href="LICENSE" target="_blank">
    <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge&logo=github" alt="MIT License">
  </a>
</p>

---

## TÜBİTAK Project

This web application is a scientific output of a **TÜBİTAK-funded research project** conducted under the ARDEB program (**Project Code: 124K233**). The project is led by **Dr. Hasan TUTAR** and aims to develop intelligent tools that support methodological decisions in qualitative research.

---

## About Q-Sat AI

Determining sample size in qualitative research often relies on **subjective criteria** such as data saturation.  
**Q-Sat AI** introduces a **data-driven, machine learning-based decision support system** to estimate optimal sample sizes objectively — without compromising the interpretive nature of qualitative inquiry.

**Purpose:**  
Q-Sat AI (Qualitative Data Saturation Estimation using AI) guides researchers in selecting sample sizes using advanced machine learning models trained on **3000+ qualitative research data points**.

---

## 📊 Technical Specifications

| Dataset | Model Architecture | Research Designs |
|---------|-----------------|-----------------|
| - 3000+ qualitative research samples<br>- 6 research designs<br>- 11 parameters<br>- 95th percentile cleaning<br>- Balanced (~500 per design) | - Ensemble Learning Models<br>- Multiple ML & meta-models<br>- Cross-validation (k=5)<br>- Avg. R² Score: 85% | - Narrative Research<br>- Ethnographic Research<br>- Phenomenology<br>- Grounded Theory<br>- Case Study<br>- Other Mixed Designs |


---

## 📈 Model Performances

| Model | Test R² Badge |
|-------|---------------|
| **KNeighbors** | ![badge](https://img.shields.io/badge/R²-0.853-brightgreen) |
| **GradientBoosting** | ![badge](https://img.shields.io/badge/R²-0.853-brightgreen) |
| **RandomForest** | ![badge](https://img.shields.io/badge/R²-0.852-brightgreen) |
| **XGBoost** | ![badge](https://img.shields.io/badge/R²-0.850-green) |
| **DecisionTree** | ![badge](https://img.shields.io/badge/R²-0.846-yellowgreen) |
| **SVR** | ![badge](https://img.shields.io/badge/R²-0.763-yellow) |
| **MLP** | ![badge](https://img.shields.io/badge/R²-0.686-orange) |
| **AdaBoost** | ![badge](https://img.shields.io/badge/R²-0.423-red) |
| **Ridge** | ![badge](https://img.shields.io/badge/R²-0.392-red) |


---

## 🧭 User Guide

1. **Select Data Quality** – Choose expected quality of your data.  
2. **Select Information Power** – Assess participant knowledge level.  
3. **Select Homogeneity/Heterogeneity** – Define group similarity/diversity.  
4. **Select Number of Interviews** – Specify interviews per participant.  
5. **Select Researcher Competence** – Rate researcher experience.  
6. **Select Research Scope** – Define narrow or broad scope.  
7. **Select Data Diversity (Triangulation)** – Assess source diversity.  
8. **Select Participant Originality** – Rate originality of insights.  
9. **Select Interview Duration** – Specify average length of interviews.  
10. **Get Prediction** – Click “Predict Sample Size” to see results.  

---

## ⚠️ Important Warnings

- Predictions are **guidance only**; not absolute.  
- Adjust based on **research topic** and **methodology**.  
- Consider **data saturation criteria**.  
- Obtain **expert opinions** and review literature.  
- Ensure **ethics committee approvals** and permissions.  

---

## 💻 Technical Details

| Technologies | Algorithms Used |
|--------------|----------------|
| Python 3.10+ | Ridge Regression |
| Scikit-learn | K-Nearest Neighbors (KNN) |
| Pandas & NumPy | Support Vector Regression (SVR) |
| Flask | Decision Tree |
| Railway | Random Forest |
|  | Gradient Boosting |
|  | AdaBoost |
|  | Neural Network (MLP) |
|  | XGBoost |

---

## 📄 License

This project is licensed under the **MIT License**.  
See [LICENSE](LICENSE) for details.

