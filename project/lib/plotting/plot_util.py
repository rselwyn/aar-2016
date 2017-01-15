import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class StockNumberBasedPlot:
	"""
	Class that plots a stock history.  All of the methods will return the object
	so that chaining methods is possible.  For example,

		graph.set_axes("X-Axis","Y-Axis").show()

	"""

	def __init__(self,name):
		"""
		Initialize the graph.
		"""
		plt.title(name)
		plt.grid(True)

	def set_axes(self, xtitle, ytitle):
		"""
		Label it.
		"""
		plt.xlabel(xtitle)
		plt.ylabel(ytitle)
		return self

	def plot_data(self, dataPoints):
		"""
		Plots stock data.  Gets the date and the "graphable_price" from the stock.  It then formats it
		in the graph.
		"""
		dates = [i.get_date() for i in dataPoints]
		y_axis = [i.get_graphable_price() for i in dataPoints]
		plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
		plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
		plt.plot(dates, y_axis)
		return self

	def plot_numbers_on_day(self, days, numbers):
		"""
		Use this to graph numbers on days.
		"""
		plt.plot(days, numbers)
		return self

	def show(self):
		"""
		Shows the graph.
		"""
		plt.gcf().autofmt_xdate()
		plt.show()
