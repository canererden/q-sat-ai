<p align="center">
  <img src="static/logo.svg" alt="Q-Sat AI Logo" width="50%" style="transition: transform 0.6s; hover:transform:rotate(10deg);">
</p>

<h1 align="center">Q-Sat AI</h1>
<h3 align="center">Machine Learning-Based Decision Support for Data Saturation in Qualitative Studies</h3>

<p align="center">
  <a href="https://q-sat-ai.up.railway.app/" target="_blank">
    <img src="https://img.shields.io/badge/Live_Demo-Visit%20Site-brightgreen?style=for-the-badge&logo=world" alt="Live Demo">
  </a>
  <a href="LICENSE" target="_blank">
    <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge&logo=github" alt="MIT License">
  </a>
</p>

---

## About

Determining sample size in qualitative research often relies on **subjective criteria** such as data saturation.  
**Q-Sat AI** introduces a **data-driven, machine learning-based decision support system** to estimate optimal sample sizes objectively — without compromising the interpretive nature of qualitative inquiry.

**Purpose:**  
Q-Sat AI is an AI-powered tool that guides researchers in selecting sample sizes using advanced machine learning models trained on **3000+ qualitative research data points**.

---

## 📊 Technical Specifications

### Dataset
- 3000+ qualitative research samples  
- 6 different research designs  
- 11 different parameters  
- 95th percentile data cleaning  
- Balanced dataset (~500 samples per design)  

### Model Architecture
- Ensemble Learning Models  
- Multiple Machine Learning & meta-models  
- Cross-validation (k=5)  
- Average R² Score: 85%  

---

## 🧪 Research Designs Supported

| Design | Description |
|--------|-------------|
| **Narrative Research** | Focus on storytelling |
| **Ethnographic Research** | Cultural analysis |
| **Phenomenology** | Experience analysis |
| **Grounded Theory** | Theory development |
| **Case Study** | In-depth examination |
| **Other Designs** | Mixed approaches |

---

## 📈 Model Performance (Detailed)

| Model | Test R² | Badge |
|-------|:-------:|:-----:|
| **KNeighbors** | 0.853 | ![badge](https://img.shields.io/badge/R²-0.853-brightgreen) |
| **GradientBoosting** | 0.853 | ![badge](https://img.shields.io/badge/R²-0.853-brightgreen) |
| **RandomForest** | 0.852 | ![badge](https://img.shields.io/badge/R²-0.852-brightgreen) |
| **XGBoost** | 0.850 | ![badge](https://img.shields.io/badge/R²-0.850-green) |
| **DecisionTree** | 0.846 | ![badge](https://img.shields.io/badge/R²-0.846-yellowgreen) |
| **SVR** | 0.763 | ![badge](https://img.shields.io/badge/R²-0.763-yellow) |
| **MLP** | 0.686 | ![badge](https://img.shields.io/badge/R²-0.686-orange) |
| **AdaBoost** | 0.423 | ![badge](https://img.shields.io/badge/R²-0.423-red) |
| **Ridge** | 0.392 | ![badge](https://img.shields.io/badge/R²-0.392-red) |

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

### Technologies
- Python 3.10+  
- Scikit-learn  
- Pandas & NumPy  
- Flask  
- Tailwind CSS  

### Algorithms Used
- Ridge Regression  
- K-Nearest Neighbors (KNN)  
- Support Vector Regression (SVR)  
- Decision Tree  
- Random Forest  
- Gradient Boosting  
- AdaBoost  
- Neural Network (MLP)  
- XGBoost  

---

## 📄 License

This project is licensed under the **MIT License**.  
See [LICENSE](LICENSE) for details.
