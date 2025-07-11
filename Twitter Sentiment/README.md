# Twitter Sentiment Analysis

I developed this machine learning project to analyze the sentiment of tweets and classify them as positive, negative, or neutral. Social media sentiment analysis can provide valuable insights into public opinion, brand perception, and trending topics.

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

Twitter is a powerful platform where users express their opinions on various topics in real time. In this project, I analyze tweet text data to detect sentiment, applying natural language processing (NLP) and machine learning techniques to classify emotions behind the tweets.

---

## Project Overview

My key objectives include:

- Cleaning and preprocessing tweet data  
- Extracting meaningful features from unstructured text  
- Applying classification algorithms to detect sentiment  
- Evaluating the models using performance metrics  

---

## Dataset

The dataset contains thousands of tweets labeled with sentiment categories such as:

- **Positive**  
- **Negative**  
- **Neutral**  

Each entry includes the tweet text and its corresponding sentiment label. I performed text cleaning by removing noise such as hashtags, mentions, URLs, and special characters.

---

## Methodology

The process involved:

- Preprocessing tweet text: tokenization, lowercasing, removing stopwords and punctuation  
- Feature extraction using CountVectorizer and TF-IDF  
- Splitting the dataset into training and test sets  
- Training models such as:  
  - Logistic Regression  
  - Naive Bayes  
  - Support Vector Machine (SVM)  
- Evaluating performance using accuracy, precision, recall, and F1-score  

---

## Results

Among all models tested, **Logistic Regression** and **SVM** achieved the highest performance, with accuracy exceeding **90%** on the test set. The models effectively captured sentiment from short, informal, and often noisy tweet text. Confusion matrices and classification reports were used to assess performance across each sentiment category.

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
