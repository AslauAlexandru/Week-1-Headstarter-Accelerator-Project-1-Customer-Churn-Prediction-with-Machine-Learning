# requirements_for_main_api.txt is for this script
# You can run the comand:
# python main_api.py

from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

# Load the XGBoost model
with open('xgb_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

# Function to preprocess new data
def preprocess_data(customer_dict):
 
  'CreditScore': customer_dict['CreditScore'],
  'Age': customer_dict['Age'],
  'Tenure': customer_dict['Tenure'],
  'Balance': customer_dict['Balance'],
  'NumOfProducts': customer_dict['NumOfProducts'],
  'HasCrCard': int(customer_dict['HasCrCard']),
  'IsActiveMember': int(customer_dict['IsActiveMember']),
  'EstimatedSalary': customer_dict['EstimatedSalary'],
  'Geography_France': 1 if customer_dict['Geography'] == 'France' else 0,
  'Geography_Germany': 1 if customer_dict['Geography'] == 'Germany' else 0,
  'Geography_Spain': 1 if customer_dict['Geography'] == 'Spain' else 0,
  'Gender_Male': 1 if customer_dict['Gender'] == 'Male' else 0,
  'Gender_Female': 1 if customer_dict['Gender'] == 'Female' else 0

  customer_df = pd.DataFrame([input_dict])

  print("customer_df")
  print(customer_df)
  
  return customer_df

# Function to get predictions
def get_predictions(customer_dict):
  preprocessed_data = preprocess_data(customer_dict)
  prediction = loaded_model.predict(preprocessed_data)
  probability = loaded_model.predict_proba(preprocessed_data)
  return prediction, probability

@app.post("/predict")
async def predict(data: dict):
  # Make prediction
  prediction, probabilities = get_predictions(data)

  return {
      "prediction": prediction.tolist(),
      "probabilities": probabilities.tolist(),
  }

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=10000)



'''
# You can try in google colab or jupyter notebook or other envirement

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


'''



