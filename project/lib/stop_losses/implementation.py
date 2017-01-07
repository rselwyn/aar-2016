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

	def __init__(self, scale_down=1.0):
		"""
			stop = HardStopLoss()

		or

			stop = HardStopLoss(scale_down=.98)
		"""
		self.scale_down =  scale_down
		self.updatedPrice = None

	def set_stop_loss_base_price(self, price):
		self.startPrice = price * self.scale_down

	def should_exit(self):
		return self.updatedPrice < self.startPrice

	def update(self, new_data):
		self.updatedPrice = new_data

	def get_current_stop(self):
		return self.startPrice

class LinearlyTrailingStopLoss(StopLoss):

	def __init__(self, max_distance):
		self.dist = max_distance

		self.currentPrice = None

	def set_stop_loss_base_price(self, price):
		self.actual_stop = price - self.dist

	def update(self, updatedPrice):
		if updatedPrice - self.dist > self.actual_stop:
			self.actual_stop = updatedPrice - self.dist

		self.currentPrice = updatedPrice

	def should_exit(self):
		return self.currentPrice < self.actual_stop

	def get_current_stop(self):
		return self.actual_stop
