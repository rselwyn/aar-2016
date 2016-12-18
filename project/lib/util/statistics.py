from __future__ import division
import numpy as np

class RatioCalculator:

	__RISK_FREE_RATE__ = 0.0

	@staticmethod
	def get_sharp_ratio(returns):
		"""
		Takes an array that represents the returns of any given strategy.
		"""
		return (MathematicalCalculator.get_mean(returnRate) - __RISK_FREE_RATE__) / MathematicalCalculator.get_std_dev(returns)

	@staticmethod
	def get_sortino_ratio(returns, stdev):


class MathematicalCalculator:

	@staticmethod
	def get_std_dev(*args):
		return np.std(np.array(args))

	@staticmethod
	def get_mean(*args):
		return np.mean(np.array(args))
