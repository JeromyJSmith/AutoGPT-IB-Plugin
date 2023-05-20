from ib_insync import *

class IBPlugin:
    def __init__(self):
        self.ib = IB()
        self.ib.connect('127.0.0.1', 7497, clientId=1)

    def get_stock_price(self, symbol):
        contract = Stock(symbol, 'SMART', 'USD')
        self.ib.qualifyContracts(contract)
        [ticker] = self.ib.reqTickers(contract)
        return ticker.marketPrice()
