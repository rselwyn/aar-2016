"""
Contains the implementation of three stop loss styles:

First: Hard Stop Loss.  Once a stock crosses this number,
the trade should be exited.

Second: Linearly trailing stop loss.  When a stock moves up,
the stop loss scales linearly with it.  When the stock goes down,
the stop loss doesn't move.

Third: Non-linear trailing stop loss.  When a stock goes up,
the stop loss trails hyperbolically.  As the gains of a trade under
this stop loss go towards infiniti, the stop loss gets closer and closer 
until it essentially becomes the price.
"""

from stop_loss import StopLoss

class HardStopLoss(StopLoss):

	def __init__(self, price, scale_down=1.0):
		"""
		This can be used in two ways.  First, directly specify the price 
		of the stop loss.  Second, specify the current stock price and by what percentage
		the stop should be at relative to the current price.

		For example, if you have a price of $100 and want your stop to be at $98 (98% of $100),
		you could do

			stop = HardStopLoss(98)

		or

			stop = HardStopLoss(100, scale_down=.98)
		"""
		self.startPrice = price * scale_down
		self.updatedPrice = None

	def should_exit(self):
		return self.updatedPrice < self.startPrice

	def update(self, new_data):
		this.updatedPrice = new_data

class LinearlyTrailingStopLoss(StopLoss):

	def __init__(self, start_price, max_distance):
		self.start = start_price
		self.dist = max_distance

		self.actual_stop = self.start - self.dist
		self.currentPrice = None

	def update(self, updatedPrice):
		if updatedPrice - self.dist > self.actual_stop:
			self.actual_stop = updatedPrice - self.dist

		self.currentPrice = updatedPrice

	def should_exit(self):
		return self.currentPrice < self.actual_stop