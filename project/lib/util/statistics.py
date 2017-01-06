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
	def get_sortino_ratio(returns):
		return (MathematicalCalculator.get_mean(returnRate) - __RISK_FREE_RATE__) / MathematicalCalculator.get_std_dev([i for i in returns if i<0])


class MathematicalCalculator:

	@staticmethod
	def get_std_dev(*args):
		return np.std(np.array(args))

	@staticmethod
	def get_mean(*args):
		return np.mean(np.array(args))

class MovingAverageCalculator:

	@staticmethod
	def get_moving_average_over_days(data_points, dayForMovingAverage):
		moving_averages_at_given_day = [] # results array
		referenceable_data_points = [] # keep track of the measured data points
		for i in data_points:
			referenceable_data_points.append(i)
			if len(referenceable_data_points) > dayForMovingAverage:
				referenceable_data_points = referenceable_data_points[1:] # remove the first element
			moving_averages_at_given_day.append(np.average(np.array([i.get_open() for i in referenceable_data_points])))

		return moving_averages_at_given_day

	@staticmethod
	def bind_moving_average_to_data_points(data_points,moving_averages, day_number):
		# Returns a modified list of stock objects where the moving averages are present
		for i,v in enumerate(moving_averages):
			data_points[i].set_nth_day_moving_average(day_number, v)

		# Pass by reference array doesn't require a return value
