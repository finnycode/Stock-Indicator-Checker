import pandas as pd
import json
import yfinance as yf
import pandas_ta as ta
import csv
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run()
