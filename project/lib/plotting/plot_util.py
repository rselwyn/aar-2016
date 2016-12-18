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
		plt.title(name)
		plt.grid(True)
	
	def set_axes(self, xtitle, ytitle):
		plt.xlabel(xtitle)
		plt.ylabel(ytitle)

	def plot_data(self, dataPoints):
		dates = [i.get_date() for i in dataPoints]
		y_axis = [i.get_open() for i in dataPoints]
		plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
		plt.gca().xaxis.set_major_locator(mdates.DayLocator())
		plt.plot(dates, y_axis)

	def show(self):
		plt.gcf().autofmt_xdate()
		plt.show()
