from ib_insync import *
import pandas as pd

class IBPlugin:
    def __init__(self):
        self.ib = IB()
        self.ib.connect('127.0.0.1', 7497, clientId=1)

    def get_stock_price(self, symbol):
        contract = Stock(symbol, 'SMART', 'USD')
        self.ib.qualifyContracts(contract)
        [ticker] = self.ib.reqTickers(contract)
        return ticker.marketPrice()

    def get_historical_data(self, symbol, durationStr='1 Y', barSizeSetting='1 day'):
        contract = Stock(symbol, 'SMART', 'USD')
        self.ib.qualifyContracts(contract)
        bars = self.ib.reqHistoricalData(
            contract,
            endDateTime='',
            durationStr=durationStr,
            barSizeSetting=barSizeSetting,
            whatToShow='TRADES',
            useRTH=True,
            formatDate=1
        )
        return util.df(bars)

    def place_order(self, symbol, action, quantity):
        contract = Stock(symbol, 'SMART', 'USD')
        self.ib.qualifyContracts(contract)
        order = MarketOrder(action, quantity)
        trade = self.ib.placeOrder(contract, order)
        return trade
