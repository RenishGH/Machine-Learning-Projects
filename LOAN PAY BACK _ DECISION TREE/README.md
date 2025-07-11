# Loan Pay Back - Decision Tree

I developed this machine learning project to predict whether a borrower will pay back their loan in full using LendingClub.com data. This prediction can help investors identify borrowers with a high probability of repayment and make informed lending decisions.

---

## Table of Contents

- Introduction  
- Project Overview  
- Dataset  
- Methodology  
- Results  
- Technologies Used  

---

## Introduction

LendingClub connects borrowers who need money with investors who provide loans. For investors, it is important to assess the likelihood that a borrower will repay their loan. This project uses historical lending data from 2007 to 2010 to build a classification model that predicts loan repayment behavior.

---

## Project Overview

My key objectives include:

- Exploring LendingClub’s publicly available loan data  
- Understanding borrower profiles and loan characteristics  
- Building a Decision Tree model to classify borrowers based on their repayment status  
- Evaluating model performance with relevant metrics  

---

## Dataset

The dataset contains cleaned LendingClub loan data from 2007-2010 with no missing values. The columns represent:

- **credit.policy**: 1 if the customer meets LendingClub's credit underwriting criteria, 0 otherwise  
- **purpose**: The purpose of the loan (e.g., credit_card, debt_consolidation, educational, etc.)  
- **int.rate**: Interest rate of the loan as a proportion (e.g., 0.11 for 11%)  
- **installment**: Monthly installment owed by the borrower  
- **log.annual.inc**: Natural log of the borrower’s self-reported annual income  
- **dti**: Debt-to-income ratio  
- **fico**: FICO credit score  
- **days.with.cr.line**: Number of days the borrower has had a credit line  
- **revol.bal**: Revolving balance on credit card  
- **revol.util**: Revolving line utilization rate  
- **inq.last.6mths**: Number of inquiries by creditors in last 6 months  
- **delinq.2yrs**: Number of 30+ days past due payments in last 2 years  
- **pub.rec**: Number of derogatory public records  

---

## Methodology

I apply a Decision Tree classifier to predict whether a borrower will fully pay back their loan. The steps include:

- Data exploration and preprocessing  
- Encoding categorical variables and handling numerical features  
- Splitting data into training and testing sets  
- Training and tuning the Decision Tree model  
- Evaluating the model with accuracy, precision, recall, and F1-score  

---

## Results

I summarize the model's predictive performance using classification metrics and visualize important insights such as feature importance and confusion matrices.

---

## Technologies Used

- Python  
- Jupyter Notebook  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Seaborn  

