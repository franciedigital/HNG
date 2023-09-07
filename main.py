
from fastapi import FastAPI, HTTPException
from typing import Optional
from data import data

app = FastAPI()

@app.get("/")
def index():
    return  {"Hello": "World"}

@app.get("/api")
def get_data(slack_name: Optional[str] = None, track: Optional[str] = None):
    if slack_name is None or track is None:
        raise HTTPException(status_code=400, detail="Both slack_name and track parameters are required")
    
    return data


