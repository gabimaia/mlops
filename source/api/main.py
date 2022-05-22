"""
Creator: Gabriel Maia
Date: May 2022
Create API
"""
# from typing import Union
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
import pandas as pd
import joblib
import os
import wandb
import sys
from source.api.pipeline import FeatureSelector, CategoricalTransformer, NumericalTransformer

# global variables
setattr(sys.modules["__main__"], "FeatureSelector", FeatureSelector)
setattr(sys.modules["__main__"], "CategoricalTransformer", CategoricalTransformer)
setattr(sys.modules["__main__"], "NumericalTransformer", NumericalTransformer)

# name of the model artifact
artifact_model_name = "Decision_tree_heart_disease/model_export:latest"

# initiate the wandb project
run = wandb.init(project="decision_tree",job_type="api")

# create the api
app = FastAPI()

# declare request example data using pydantic
# a person in our dataset has the following attributes
class Person(BaseModel):
    age: int
    Sex: str
    ChestPainType: str
    RestingBP: int
    Cholesterol: int
    FastingBS: int
    RestingECG: str	
    MaxHR: int
    ExerciseAngina: str	
    Oldpeak: float	
    ST_Slope: str

    class Config:
        schema_extra = {
            "example": {
                "Age": 72,
                "sex": 'M',
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
        }
        #"Age	Sex	ChestPainType	RestingBP	Cholesterol	FastingBS	RestingECG	MaxHR	ExerciseAngina	Oldpeak	ST_Slope"

# give a greeting using GET
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <p><span style="font-size:28px"><strong>Hello World</strong></span></p>"""\
    """<p><span style="font-size:20px">In this project, we will apply the skills """\
        """acquired in the Deploying a Scalable ML Pipeline in Production course to develop """\
        """a classification model on publicly available"""\
        """<a href="https://archive.ics.uci.edu/ml/datasets/statlog+(heart)"></a>.</span></p>"""

# run the model inference and use a Person data structure via POST to the API.
@app.post("/predict")
async def get_inference(person: Person):
    
    # Download inference artifact
    model_export_path = run.use_artifact(artifact_model_name).file()
    pipe = joblib.load(model_export_path)
    
    # Create a dataframe from the input feature
    # note that we could use pd.DataFrame.from_dict
    # but due be only one instance, it would be necessary to
    # pass the Index.
    df = pd.DataFrame([person.dict()])

    # Predict test data
    predict = pipe.predict(df)

    return "HeartDisease" if predict[0] <= 0.5 else "NoHeartDisease"