from abc import ABCMeta, abstractmethod

class TradingStrategy(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def shouldBuy(self, initialDataPoint, secondaryDataPoint):
		raise NotImplementedError