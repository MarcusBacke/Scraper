import yfinance as yf
from fastapi import FastAPI
from yfinance import ticker

app = FastAPI()

@app.get('/stockInfo/{ticker}')
async def yInformation(ticker): 
    msft = yf.Ticker(ticker).info
    return msft
    

