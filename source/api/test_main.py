"""
Creator: Ivanovitch Silva
Date: 18 April 2022
API testing
"""
from fastapi.testclient import TestClient
import os
import sys
import pathlib
from source.api.main import app

# Instantiate the testing client with our app.
client = TestClient(app)

# a unit test that tests the status code of the root path
def test_root():
    r = client.get("/")
    assert r.status_code == 200

# a unit test that tests the status code and response 
# for an instance with no heart disease
'''def test_get_inference():

    person = {
        "Age": 54,
        "Sex": 'F',
        "ChestPainType": 'NAP',
        "RestingBP": 135,
        "Cholesterol": 304,
        "FastingBS": 1,
        "RestingECG": 'Normal',
        "MaxHR": 170,
        "ExerciseAngina": 'N',
        "Oldpeak": 0.0,	
        "ST_Slope": 'Up',
    }

    r = client.post("/predict", json=person)
    # print(r.json())
    assert r.status_code == 200
    assert r.json() == "Heart Disease"

# a unit test that tests the status code and response 
# for an instance with a heart disease
def test_get_inference():

    person = {
        "Age": 60,
        "Sex": 'M',
        "ChestPainType": 'NAP',
        "RestingBP": 115,
        "Cholesterol": 100,
        "FastingBS": 1,
        "RestingECG": 'Normal',
        "MaxHR": 143,
        "ExerciseAngina": 'N',
        "Oldpeak": 2.4,
        "ST_Slope": 'Up',
    }

    r = client.post("/predict", json=person)
    print(r.json())
    assert r.status_code == 200
    assert r.json() == "No Heart Disease"'''
