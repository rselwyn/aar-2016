"""
Collects data using the pandas datareader.
"""

import pandas_datareader.data as web
import datetime
from ..models.stock_model import StockOHLCV
from ..util.statistics import MovingAverageCalculator

class PandasBasedDataReader:

	def __init__(self, first, second, symbol):
		"""
		Initialize with the first day, second day, and the ticker symbol.
		"""
		self.start = first
		self.end = second
		self.symbol = symbol

	def get_data(self, calculate_moving_averages=[]):
		"""
		Has an optional parameter for the days on which the moving averages should be calculated for.  By default,
		no moving averages should be calculated.
		"""

		# Returns PD Dataframe that looks like
		# Index([u'Open', u'High', u'Low', u'Close', u'Volume', u'Adj Close'], dtype='object')
		allData = web.DataReader(self.symbol, 'yahoo', self.start, self.end)
		outputList = []
		for index,row in allData.iterrows():
			outputList.append(StockOHLCV(index.to_datetime(),row["Open"],row["High"], row["Low"], row["Close"], row["Volume"], self.symbol))

		# Get the moving averages
		for i in calculate_moving_averages:
			averages = MovingAverageCalculator.get_moving_average_over_days(outputList,i)

			for number in range(len(outputList)):
				outputList[number].set_nth_day_moving_average(i, averages[number])

		return outputList
