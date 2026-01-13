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
