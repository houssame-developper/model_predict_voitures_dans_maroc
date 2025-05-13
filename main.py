from fastapi import FastAPI
from joblib import load
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np

from typing import Optional

class Item(BaseModel):
    vile: str
    year: float
    transmission: str
    fuel: str
    mileage: float
    marque: str
    model: str
    doors: str
    premiere_main: str
    puissance_fiscale: str
    etat: str
    orgine: str
    ABS: Optional[str] = "0"
    Airbags: Optional[str] = "0"
    CD_MP3_Bluetooth: Optional[str] = "0"
    Caméra_de_recul: Optional[str] = "0"
    Climatisation: Optional[str] = "0"
    ESP: Optional[str] = "0"
    Jantes_aluminium: Optional[str] = "0"
    Limiteur_de_vitesse: Optional[str] = "0"
    Ordinateur_de_bord: Optional[str] = "0"
    Radar_de_recul: Optional[str] = "0"
    Régulateur_de_vitesse: Optional[str] = "0"
    Sièges_cuir: Optional[str] = "0"
    Système_de_navigation_GPS: Optional[str] = "0"
    Toit_ouvrant: Optional[str] = "0"
    Verrouillage_centralisé_à_distance: Optional[str] = "0"
    Vitres_électriques: Optional[str] = "0"
    

# السماح لجميع المصادر (في التطوير فقط)

app=FastAPI()


# السماح لمنشأ معين فقط (localhost:3000)
origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "http://127.0.0.1:3000/c:/Users/bouyo/Pictures/tempr/",
    "file:///C:/Users/bouyo/Pictures/tempr/index.html"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # لا تضع ["*"] هنا لأنك تسمح بـ credentials
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = load("catboost_model1.joblib")

cars= pd.read_csv("cars_cleaned.csv")
cars=cars.dropna()
@app.post("/")
def read_root(item: Item):

    # إنشاء DataFrame
# إنشاء DataFrame
   data = pd.DataFrame([{
    'year': item.year,
    'mileage': item.mileage,
    'transmission': item.transmission,
    'fuel': item.fuel,
    'marque': item.marque,
    'model': item.model,
    'vile': item.vile,
    'premiere_main': item.premiere_main,
    'puissance_fiscale': item.puissance_fiscale,
    'etat': item.etat.capitalize(),
    'orgine': item.orgine,
    'ABS': item.ABS,
    'Airbags': item.Airbags,
    'CD/MP3/Bluetooth': item.CD_MP3_Bluetooth,
    'Caméra de recul': item.Caméra_de_recul,
    'Climatisation': item.Climatisation,
    'ESP': item.ESP,
    'Jantes aluminium': item.Jantes_aluminium,
    'Limiteur de vitesse': item.Limiteur_de_vitesse,
    'Ordinateur de bord': item.Ordinateur_de_bord,
    'Radar de recul': item.Radar_de_recul,
    'Régulateur de vitesse': item.Régulateur_de_vitesse,
    'Sièges cuir': item.Sièges_cuir,
    'Système de navigation/GPS': item.Système_de_navigation_GPS,
    'Toit ouvrant': item.Toit_ouvrant,
    'Verrouillage centralisé à distance': item.Verrouillage_centralisé_à_distance,
    'Vitres électriques': item.Vitres_électriques,
    'doors': item.doors
}])
   price= model.predict(data).tolist()[0]
   price = round(np.expm1(price), 2)
   return {"total":price}   


@app.get("/viles")
def get_vile(): 
    vile = cars['vile'].unique().tolist()
    return {"elements": vile}

@app.get("/marques")
def get_marque():
    marque = cars['marque'].unique().tolist()
    return {"elements": marque}
@app.get("/models")
def get_model():
    model = cars['model'].unique().tolist()
    return {"elements": model}

