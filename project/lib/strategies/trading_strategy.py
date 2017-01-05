from abc import ABCMeta, abstractmethod

class TradingStrategy(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def should_buy(self, initialDataPoint, secondaryDataPoint):
		raise NotImplementedError
