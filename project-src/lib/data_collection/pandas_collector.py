"""
Collects data using the pandas datareader.
"""

import pandas_datareader.data as web
import datetime
from ..models.stock_model import StockOHLCV

class PandasBasedDataReader:

	def __init__(self, first, second, symbol):
		self.start = first
		self.end = end
		self.symbol = symbol

	def get_data(self):
		# Returns PD Dataframe that looks like
		# Index([u'Open', u'High', u'Low', u'Close', u'Volume', u'Adj Close'], dtype='object')
		allData = web.datareader(self.symbol, 'yahoo', self.start, self.end)
		outputList = []
		for index,row in f.iterrows():
			outputList.append(StockOHLCV(index,row["Open"],row["High"], row["Low"], row["Close"], row["Volume"]))

		return outputList