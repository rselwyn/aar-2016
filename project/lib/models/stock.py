from abc import ABCMeta, abstractmethod

class StockModel(object):

	__metaclass__ = ABCMeta

	@abstractmethod
	def get_graphable_price(self):
		raise NotImplementedError

	@abstractmethod
	def get_date(self, new_piece_of_data):
		raise NotImplementedError