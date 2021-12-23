
from typing import Mapping
from fastapi import FastAPI
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
app = FastAPI()

@app.get('/btc')
async def get_btc_price():
    message = cg.get_price(ids='bitcoin', vs_currencies='usd')
    return message

@app.get('/eth')
async def get_btc_price():
    message = cg.get_price(ids='ethereum', vs_currencies='usd')
    return message

@app.get("/")
async def root():
    return {"message": "Hello World"}
