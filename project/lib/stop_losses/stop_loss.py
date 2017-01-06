from abc import ABCMeta, abstractmethod

class StopLoss(object):

	__metaclass__ = ABCMeta

	@abstractmethod
	def set_stop_loss_base_price(self, price):
		"""
		The simulator will call this method with the price at which
		it is about to buy.
		"""
		raise NotImplemented

	@abstractmethod
	def should_exit(self):
		"""
		Should return a boolean of whether the
		trade should be exited.
		"""
		raise NotImplementedError

	@abstractmethod
	def update(self, new_piece_of_data):
		"""
		Provide new data to the stop loss object.  Use this
		to provide new pricing data.
		"""
		raise NotImplementedError

	@abstractmethod
	def get_current_stop(self):
		"""
		Called by the simulator to get the current stop-loss price.
		"""
		raise NotImplementedError
