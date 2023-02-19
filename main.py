import pandas as pd
import json
import yfinance as yf
import pandas_ta as ta
import csv

f = open('constituents.json')
constituents_data = json.load(f)

name_data = pd.DataFrame(constituents_data)

print(name_data['Symbol'])


class stockAvatar:
    def __init__(self, symbol_):
        self.symbol = symbol_

    def getPriceData1m(self):
        self.price_data = yf.download(self.symbol, start="2023-02-15", end="2023-02-18", interval="1m")

    def getPriceData5m(self):
        self.price_data = yf.download(self.symbol, start="2023-02-15", end="2023-02-18", interval="5m")



    def calcRSI(self):
        self.rsi = ta.rsi((self.price_data['Close']))
        self.last_rsi = self.rsi.iloc[-1]

    def calcADX(self):
        self.adx = ta.adx(self.price_data['High'], self.price_data['Low'], self.price_data['Close'], length=14)[
            'ADX_14']
        self.last_adx = self.adx.iloc[-1]


output_list = []

for element in name_data['Symbol']:
    try:
        stock_info = stockAvatar(element)
        stock_info.getPriceData1m()
        stock_info.calcRSI()
        stock_info.calcADX()

        if stock_info.last_rsi > 70 and stock_info.last_adx > 20:
            output_list.append([['1m'],['ABOVE'],['Symbol: ', stock_info.symbol], ['RSI: ', stock_info.last_rsi], ['ADX: ', stock_info.last_adx]])
        if stock_info.last_rsi < 30 and stock_info.last_adx > 20:
            output_list.append([['1m'],['BELOW'],['Symbol: ', stock_info.symbol], ['RSI: ', stock_info.last_rsi], ['ADX: ', stock_info.last_adx]])

        stock_info = stockAvatar(element)
        stock_info.getPriceData5m()
        stock_info.calcRSI()
        stock_info.calcADX()

        if stock_info.last_rsi > 70 and stock_info.last_adx > 20:
            output_list.append([['5m'],['ABOVE'],['Symbol: ', stock_info.symbol], ['RSI: ', stock_info.last_rsi], ['ADX: ', stock_info.last_adx]])
        if stock_info.last_rsi < 30 and stock_info.last_adx > 20:
            output_list.append([['5m'],['BELOW'],['Symbol: ', stock_info.symbol], ['RSI: ', stock_info.last_rsi], ['ADX: ', stock_info.last_adx]])

    except:
        pass
output_list = pd.DataFrame(output_list)


output_list.to_csv('scrape_output.csv')





