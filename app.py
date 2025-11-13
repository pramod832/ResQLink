
from fastapi import FastAPI
import json

app = FastAPI(title="LifeLine Global – Emergency Resource Locator")

data=json.load(open("data.json","r"))

@app.get("/")
def home():
    return {"status":"ok","message":"LifeLine Global API running"}

@app.get("/resources/{country}/{city}")
def get_resources(country:str, city:str):
    country=country.lower()
    city=city.lower()
    if country in data and city in data[country]:
        return data[country][city]
    return {"error":"Location not found"}
