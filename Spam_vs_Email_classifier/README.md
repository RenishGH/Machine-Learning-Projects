# Spam vs Email Classifier

I developed this machine learning project to classify emails as either spam or legitimate (ham). With the ever-increasing volume of emails, building an accurate spam detection system is essential to improve productivity and reduce the risk of phishing or malicious content.

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

Spam detection is a classic and practical application of machine learning. In this project, I analyze text data from emails and build classification models to distinguish between spam and non-spam messages based on their content.

---

## Project Overview

My key objectives include:

- Preprocessing raw email text data  
- Extracting relevant features using NLP techniques  
- Applying classification algorithms to detect spam  
- Evaluating the models with appropriate performance metrics  

---

## Dataset

The dataset consists of labeled emails with two classes:

- **spam**: Unwanted or potentially harmful messages  
- **ham**: Legitimate, non-spam emails  

Each email contains unstructured text, which I clean and convert into numerical features suitable for training classification models.

---

## Methodology

I followed these steps to build the spam classifier:

- Text cleaning: Lowercasing, removing punctuation and stopwords  
- Tokenization and vectorization using methods like CountVectorizer or TF-IDF  
- Splitting data into training and test sets  
- Training multiple classification models including:  
  - Multinomial Naive Bayes  
  - Logistic Regression  
  - Support Vector Machine (SVM)  
- Evaluating using accuracy, precision, recall, and F1-score  

---

## Results

The spam classifier models performed very well, with the **Multinomial Naive Bayes** and **SVM** models achieving over **95% accuracy** on the test set. Precision and recall were high, especially for detecting spam correctly while minimizing false positives. Visualizations like confusion matrices and ROC curves helped validate model effectiveness.

---

## Technologies Used

- Python  
- Jupyter Notebook  
- Pandas  
- NumPy  
- Scikit-learn  
- NLTK / spaCy  
- Matplotlib  
- Seaborn  

---

## Contact

Feel free to check out my portfolio at [https://renishmirani.carrd.co/](https://renishmirani.carrd.co/)  
or reach out to me via email: miranirenish25@gmail.com
