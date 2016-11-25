

class StockOHLCV:
	"""
	Class that models one day stock information (Open, High, Low, Close, Volume)
	"""

	def __init__(self, date, stockOpen, stockHigh, stockLow, stockClose, volume):
		self.date = date
		self.stockOpen = stockOpen
		self.stockHigh = stockHigh
		self.stockLow = stockLow
		self.stockClose = stockClose
		self.volume = volume

	def get_open(self):
		return self.stockOpen

	def get_close(self):
		return self.stockClose

	def get_high(self):
		return self.stockHigh

	def get_low(self):
		return self.stockLow

	def get_volume(self):
		return self.volume

	def get_date(self):
		return self.date
