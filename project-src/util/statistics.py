from __future__ import division
import numpy as np

class RatioCalculator:

	__RISK_FREE_RATE__ = 0.0

	@staticmethod
	def get_sharp_ratio(returnRate, stdev):
		return (returnRate - __RISK_FREE_RATE__) / stdev

class MathematicalCalculator:

	@staticmethod
	def get_std_dev(*args):
		return np.std(np.array(args))

	@staticmethod
	def get_mean(*args):
		return np.mean(np.array(args))