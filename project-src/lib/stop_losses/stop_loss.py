from abc import ABCMeta, abstractmethod

class StopLoss(object):

	__metaclass__ = ABCMeta

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