from abc import ABCMeta, abstractmethod

class TradingStrategy(object):
	"""
	Abstract class that all trading strategies will extend for polymorphism (so that the strategy_runner can run
	all types of trading strategies).
	"""

	__metaclass__ = ABCMeta

	@abstractmethod
	def should_buy(self, initialDataPoint, secondaryDataPoint):
		raise NotImplementedError

	@abstractmethod
	def should_sell(self, initialDataPoint, secondaryDataPoint):
		raise NotImplementedError