# Energy Usage Prediction

This repository contains a machine learning project focused on predicting **energy consumption** based on various environmental and temporal features. Energy usage forecasting plays a crucial role in energy management, load balancing, and sustainability planning.

---

## Table of Contents

- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Usage](#usage)
- [Results](#results)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

As global energy demands rise, the ability to predict future usage accurately is essential for optimizing energy distribution and reducing operational costs. This project explores various machine learning regression techniques to forecast energy usage using environmental data such as temperature, humidity, time of day, and seasonality.

---

## Project Overview

The main objectives of this project include:

- Analyzing historical energy consumption data
- Building predictive models to estimate future energy usage
- Identifying the most influential features affecting energy demand
- Visualizing patterns and trends in energy consumption

---

## Dataset

The dataset contains historical records of energy usage along with contextual variables such as:

- **Temperature**
- **Humidity**
- **Time of Day**
- **Day of Week**
- **Weather Conditions**
- **Energy Usage** (target variable)

The dataset was cleaned, and missing values were handled appropriately.

---

## Methodology

This project implements several regression models to predict energy consumption:

- Linear Regression  
- Decision Tree Regressor  
- Random Forest Regressor  
- Gradient Boosting Regressor  

### Preprocessing Steps:

- Handling missing values  
- Feature encoding  
- Feature scaling  
- Train-test split and cross-validation

### Evaluation Metrics:

- Mean Absolute Error (MAE)  
- Mean Squared Error (MSE)  
- Root Mean Squared Error (RMSE)  
- R² Score  

---


# Clone the repository
git clone https://github.com/RenishGH/Machine-Learning-Projects.git
cd Machine-Learning-Projects/Energy\ Usage\ Prediction

---


## Results
The model performance was evaluated using multiple regression metrics. Visualizations include:

- Feature importance  
- Actual vs. Predicted plots  
- Time series trends  

## Technologies Used
- Python  
- Jupyter Notebook  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Seaborn  
