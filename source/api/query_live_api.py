"""
Creator: Ivanovitch Silva
Date: 26 April. 2022
Script that POSTS to the API using the requests 
module and returns both the result of 
model inference and the status code
"""
import requests
import json
# import pprint

person = {
        "Age": 72,
        "Sex": 'M',
        "ChestPainType": 'NAP',
        "RestingBP": 120,
        "Cholesterol": 304,
        "FastingBS": 1,
        "RestingECG": 'Normal',
        "MaxHR": 120,
        "ExerciseAngina": 'Y',
        "Oldpeak": 1.0,
        "ST_Slope": 'Up',
    }

url = "http://127.0.0.1:8000"
#url = "https://heart-disease-appx.herokuapp.com/"
response = requests.post(f"{url}/predict",
                         json=person)

print(f"Request: {url}/predict")
print(f"Person: \n Age: {person['Age']}\n sex: {person['sex']}\n"\
      f" ChestPainType: {person['ChestPainType']}\n RestingBP: {person['RestingBP']}\n"\
      f" Cholesterol: {person['Cholesterol']}\n"\
      f" FastingBS: {person['FastingBS']}\n"\
      f" RestingECG: {person['RestingECG']}\n"\
      f" MaxHR: {person['MaxHR']}\n"\
      f" ExerciseAngina: {person['ExerciseAngina']}\n"\
      f" Oldpeak: {person['Oldpeak']}\n"\
      f" ST_Slope: {person['ST_Slope']}\n"
     )
print(f"Result of model inference: {response.json()}")
print(f"Status code: {response.status_code}")
