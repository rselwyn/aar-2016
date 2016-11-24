

class StockOHLCV:
	"""
	Class that models one day stock information (Open, High, Low, Close, Volume)
	"""

	def __init__(self, stockOpen, stockHigh, stockLow, stockClose, volume):
		self.stockOpen = stockOpen
		self.stockHigh = stockHigh
		self.stockLow = stockLow
		self.stockClose = stockClose
		self.volume = volume

	def getOpen(self):
		return self.stockOpen

	def getClose(self):
		return self.stockClose

	def getHigh(self):
		return self.stockHigh

	def getLow(self):
		return self.stockLow

	def getVolume(self):
		return self.volume
