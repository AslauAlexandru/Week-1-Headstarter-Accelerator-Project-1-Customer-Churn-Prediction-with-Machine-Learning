# Week 1 Headstarter Accelerator Project 1: Customer Churn Prediction with Machine Learning
Week 1: Customer Churn Prediction with Machine Learning
In this project, you will build an end-to-end pipeline for a customer churn prediction model. You will learn how to load in the dataset, clean the data, train 5 different ML models, perform hyperparameter tuning, and serve the model for inference through a web app.

[Churn for Bank Customers](https://www.kaggle.com/datasets/mathchi/churn-for-bank-customers) Dataset from Kaggle. Predict customer churn in a bank. 

## About Dataset
**Content**
- RowNumber—corresponds to the record (row) number and has no effect on the output.
- CustomerId—contains random values and has no effect on customer leaving the bank.
- Surname—the surname of a customer has no impact on their decision to leave the bank.
- CreditScore—can have an effect on customer churn, since a customer with a higher credit score is less likely to leave the bank.
- Geography—a customer’s location can affect their decision to leave the bank.
- Gender—it’s interesting to explore whether gender plays a role in a customer leaving the bank.
- Age—this is certainly relevant, since older customers are less likely to leave their bank than younger ones.
- Tenure—refers to the number of years that the customer has been a client of the bank. Normally, older clients are more loyal and less likely to leave a bank.
- Balance—also a very good indicator of customer churn, as people with a higher balance in their accounts are less likely to leave the bank compared to those with lower balances.
- NumOfProducts—refers to the number of products that a customer has purchased through the bank.
- HasCrCard—denotes whether or not a customer has a credit card. This column is also relevant, since people with a credit card are less likely to leave the bank.
- IsActiveMember—active customers are less likely to leave the bank.
- EstimatedSalary—as with balance, people with lower salaries are more likely to leave the bank compared to those with higher salaries.
- Exited—whether or not the customer left the bank.

## Steps for run
[Customer Churn Prediction with Machine Learning](https://colab.research.google.com/drive/1mpzJq3KFtJo6nFICotTI6ZHg7wrr3p9u?usp=sharing) (google colab) and [web app](https://github.com/AslauAlexandru/Week-1-Headstarter-Accelerator-Project-1-Customer-Churn-Prediction-with-Machine-Learning/blob/main/main.py).
First I run in the google colab (or in jupyter notebook local), after that download the machine learning models as .pkl pickle. Second I upload the machine learning models as .pkl pickle to Replit (or in other evironment). In my case I use these steps. Google colab [*Week_1_Headstarter_Accelerator_Project_1_Customer_Churn_Prediction_with_Machine_Learning.ipynb*](https://colab.research.google.com/drive/1mpzJq3KFtJo6nFICotTI6ZHg7wrr3p9u?usp=sharing) and [web app](https://github.com/AslauAlexandru/Week-1-Headstarter-Accelerator-Project-1-Customer-Churn-Prediction-with-Machine-Learning/blob/main/main.py) [*main.py*](https://github.com/AslauAlexandru/Week-1-Headstarter-Accelerator-Project-1-Customer-Churn-Prediction-with-Machine-Learning/blob/main/main.py).


## Web application with streamlit
I use Replit for [web application](https://github.com/AslauAlexandru/Week-1-Headstarter-Accelerator-Project-1-Customer-Churn-Prediction-with-Machine-Learning/blob/main/main.py).
The [web app](https://github.com/AslauAlexandru/Week-1-Headstarter-Accelerator-Project-1-Customer-Churn-Prediction-with-Machine-Learning/blob/main/main.py) utilizes the following machine learning models for churn prediction:
- **XGBoost**
- **Random Forest**
- **K-Nearest Neighbors**
- **Support Vector Machine**
- **Gradient Boosting**
- **optional to use**: **Decision Tree** and **Naive Bays**

## Web app via API (optional)
I haven't had time to test the code from [*main_api.py*](https://github.com/AslauAlexandru/Week-1-Headstarter-Accelerator-Project-1-Customer-Churn-Prediction-with-Machine-Learning/blob/main/main_api.py).
You can find web app via API code in [*main_api.py*](https://github.com/AslauAlexandru/Week-1-Headstarter-Accelerator-Project-1-Customer-Churn-Prediction-with-Machine-Learning/blob/main/main_api.py) and other code with ```FastAPI```. You can try this code, but replace with your URL:
```python
# You can try in google colab or jupyter notebook or other environment

import requests
import json

# URL of your deployed model
url = "https://churn-ml-models.onrender.com/predict"

# Sample customer data
customer_data = {
    "CreditScore": 200,
    "Geography": "France",
    "Gender": "Male",
    "Age": 35,
    "Tenure": 0,
    "Balance": 0,
    "NumOfProducts": 3,
    "HasCrCard": 1,
    "IsActiveMember": 0,
    "EstimatedSalary": 8
}

# Send POST request
response = requests.post(url, json=customer_data)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    result = response.json()
    print(result)
else:
    print("Error:", response.status_code, response.text)
```




























