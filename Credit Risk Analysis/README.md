# Credit Risk Analysis

This repository contains a machine learning project focused on **credit risk prediction** — identifying whether a loan applicant is likely to default. This type of analysis is critical for financial institutions to manage lending risk and maintain profitability.

---

## Table of Contents

- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

Credit risk analysis is a common use case in financial machine learning. It involves predicting the likelihood that a borrower will default on a loan based on various features such as income, credit history, loan amount, and more. This project demonstrates how machine learning can be used to build a classification model that helps financial institutions assess risk and make informed lending decisions.

---

## Project Overview

The key objectives of this project are:

- Clean and preprocess credit-related data
- Handle class imbalance (e.g., using SMOTE, undersampling)
- Train classification models to distinguish between risky and safe loans
- Evaluate model performance using appropriate metrics

---

## Dataset

The dataset used contains features relevant to loan applications and borrower profiles, such as:

- **Applicant Features**: Age, Income, Employment Status, Credit Score  
- **Loan Details**: Loan Amount, Interest Rate, Purpose, Term  
- **Target Variable**: Loan Status — e.g., `Fully Paid` vs. `Charged Off` (or `Good` vs. `Bad` credit)

> Example:  
> The dataset was sourced from [Kaggle/UCI/Internal Source].  
> It contains `X` rows and `Y` columns.

---

## Methodology

We implemented several machine learning models to predict credit risk, including:

- Logistic Regression  
- Decision Tree Classifier  
- Random Forest Classifier  
- Balanced Random Forest  
- Easy Ensemble Classifier  
- [Add more if applicable]

### Preprocessing Steps:

- Handling missing values  
- Encoding categorical variables  
- Addressing class imbalance using:
  - SMOTE (Synthetic Minority Over-sampling Technique)
  - Random Undersampling
- Feature scaling (if needed)

### Model Evaluation:

- Confusion Matrix  
- Accuracy  
- Precision, Recall, F1-score  
- AUC-ROC Score

---

## Installation

```bash
# Clone the repository
git clone https://github.com/RenishGH/Machine-Learning-Projects.git
cd Machine-Learning-Projects/Credit\ Risk\ Analysis

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required libraries
pip install -r requirements.txt

Results
Key performance metrics (example):
Best Model: Easy Ensemble Classifier
Accuracy: 93%
Recall for High-Risk Class: 92%
AUC-ROC Score: 0.89
