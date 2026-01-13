# Scholastic Model Monitor: Student Performance Prediction

## Overview

This machine learning project creates a complete system to forecast student academic success, specifically focusing on Math scores. By analyzing demographic data, social factors, and prior academic results, the system identifies students who may require additional support and provides insights into the variables that most influence academic outcomes.

### Why Academic Monitoring is Crucial

- **Early Intervention**: Identifying students at risk of low performance allows educators to step in with tutoring before final examinations.
- **Resource Optimization**: Helps schools allocate teaching assistants and study materials to the demographic groups or subjects where they are needed most.
- **Informed Policy**: Understand how factors like test preparation courses or parental education levels impact actual classroom results.
- **Data-Driven Success**: Moving from intuitive teaching to evidence-based academic support.

---

## Features

### Core Functionality
- **ML-Powered Predictions**: High-accuracy regression models including XGBoost and CatBoost.
- **Modular Pipeline**: Clean separation between data ingestion, transformation, and training components.
- **Automated Preprocessing**: Custom pipelines for handling missing data and feature scaling.
- **Custom Exception Handling**: Real-time error tracking with script name and line number reporting.
- **Artifact Management**: Automated serialization of preprocessor and model objects.

### Key Capabilities
- Automated Train-Test splitting of raw student datasets.
- Handling of both numerical and categorical feature sets.
- Scalable architecture for adding new academic features.
- Logging of every execution step for MLOps traceability.

---

## Dataset

The system uses a student performance dataset containing comprehensive academic and social information:

### Dataset Statistics
- **Features**: 8 input variables (Categorical and Numerical)
- **Target**: Continuous variable (`math_score`)
- **Category**: Regression task

### Feature Categories

#### 1. Demographic Information
- `gender`: Student gender.
- `race_ethnicity`: Five distinct ethnic groups.

#### 2. Socio-Economic Factors
- `parental_level_of_education`: Educational background of parents.
- `lunch`: Type of lunch program (Standard or Free/Reduced).

#### 3. Academic Preparation
- `test_preparation_course`: Status of course completion (Completed/None).

#### 4. Historical Scores (Numerical)
- `reading_score`: Performance in reading assessments.
- `writing_score`: Performance in writing assessments.

---

## Installation

### Prerequisites

```bash
Python 3.8 or higher
pip (latest version)
Git
```
### 1. Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```
### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## Project Structure
```
Scholastic_model_monitor/
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py      # Data loading and train-test splitting
│   │   ├── data_transformation.py # Pipeline for scaling and encoding
│   │   └── model_trainer.py       # Model training and hyperparameter tuning
│   │
│   ├── pipeline/
│   │   ├── train_pipeline.py      # Triggers the training workflow
│   │   └── predict_pipeline.py    # Logic for real-time predictions
│   │
│   ├── logger.py                  # Pipeline execution tracking
│   ├── exception.py               # Custom error handling
│   └── utils.py                   # Helper functions (save/load objects)
│
├── artifacts/                     # Stores processed data and .pkl files
├── notebook/                      # EDA and Model experiments
├── requirements.txt               # Project dependencies
└── setup.py                       # Project metadata and packaging
```

## Input parameters

| Parameter | Type | Range/Options | Description |
| :--- | :--- | :--- | :--- |
| Reading Score | Integer | 0-100 | Previous reading test score |
| Writing Score | Integer | 0-100 | Previous writing test score |
| Gender | Dropdown | Male/Female | Student gender |
| Ethnicity | Dropdown | Group A-E | Racial/Ethnic background |
| Parental Education | Dropdown | Degree levels | Parent's highest education |
| Lunch | Dropdown | Standard/Reduced | Socio-economic indicator |
| Prep Course | Dropdown | Completed/None | Test preparation status |

## Model Details

### Machine Learning Pipeline
`Raw CSV` → `Data Ingestion` → `Preprocessing (Impute & Scale)` → `Model Training` → `Serialization`



### 1. Data Preprocessing

**Encoding Strategy**

| Feature Type | Method | Example |
| :--- | :--- | :--- |
| **Numerical** | `StandardScaler` | $\frac{x - \mu}{\sigma}$ |
| **Categorical** | `One-Hot Encoding` | Gender → `[1, 0]` |
| **Missing Values** | `SimpleImputer` | Median (Num), Most Frequent (Cat) |



### 2. Model Architecture
The system uses a **Stacked Regression Approach** to maximize accuracy:

* **XGBoost Regressor**: Handles non-linear relationships and high-dimensional data.
* **CatBoost Regressor**: Optimized for categorical feature handling without manual encoding.
* **Hyperparameter Tuning**: Utilizes `GridSearchCV` to find the best estimator parameters.

## Technologies Used

### Core Technologies
* **Python 3.8+**: Primary programming language
* **Pandas/NumPy**: Data manipulation and numerical analysis
* **scikit-learn**: Preprocessing and pipeline management
* **XGBoost/CatBoost**: Gradient boosting frameworks
* **Dill/Pickle**: Model and pipeline serialization

### Development Tools
* **Git**: Version control
* **VS Code**: IDE
* **Jupyter Notebook**: Exploratory Data Analysis


## Acknowledgments
* Inspired by modern MLOps practices for production-ready code.
* **Dataset**: Educational records for research in academic performance.
* Special thanks to the open-source community for Scikit-Learn and Gradient Boosting libraries.


## Future Roadmap

### Version 1.1 (Q1 2026)
- [ ] Integration of a Streamlit web dashboard for teachers.
- [ ] Model explainability using SHAP values.
- [ ] Deployment to AWS/Azure using Docker containers.
