from ib_insync import *
import pandas as pd

class IBBacktestPlugin:
    def __init__(self):
        self.ib = IB()
        self.ib.connect('127.0.0.1', 7497, clientId=1)

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

    def simulate_trade(self, symbol, action, quantity):
        # This is a simplified simulation, you may need a more complex simulation for your backtest
        contract = Stock(symbol, 'SMART', 'USD')
        self.ib.qualifyContracts(contract)
        [ticker] = self.ib.reqTickers(contract)
        price = ticker.marketPrice()
        return price * quantity if action == 'BUY' else -price * quantity

    def calculate_performance(self, trades):
        # This is a simplified calculation, you may need a more complex calculation for your backtest
        return sum(trades)
