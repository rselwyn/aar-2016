import numpy as np
import matplotlib.pyplot as plt

class StockNumberBasedPlot(object):

	def __init__(self,name):
		plt.title(name)
	
	def set_axes(self, xtitle, ytitle):
		plt.xlabel(xtitle)
		plt.ylabel(ytitle)

	def plot_data(self, dataPoints):
		pass

	def show(self):
		plt.gcf().autofmt_xdate()
		plt.show()