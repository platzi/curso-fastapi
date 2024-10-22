import zoneinfo
from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel


class Customer(BaseModel):
    name: str
    description: str | None
    email: str
    age: int


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hola, Luis!"}


country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
}


@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    return {"time": datetime.now(tz)}


@app.post("/customers")
async def create_customer(customer_data: Customer):
    return customer_data
