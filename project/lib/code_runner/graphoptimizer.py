
class GraphOptimizer(object):

	def __init__(self, dataMap):
		"""
		dataMap should be in the form of {decimal value: profit}
		"""
		self.data = dataMap

		self.data_list = []

		for i,v in self.data:
			self.data_list.append(v)


	def getAbsoluteMax(self):
		return max(self.data, key=lambda i:i[1])[1]

	def get_max_position(self):
		return [i for i, j in enumerate(self.data) if j[1] == self.getAbsoluteMax()][0]

	def getNinetyPercentDistance(self):
		data_filtered_to_ninety = filter(lambda i: i[1] > (.9 * self.getAbsoluteMax()), self.data)
		return data_filtered_to_ninety[-1][0] - data_filtered_to_ninety[0][0]

	def getSmoothedMax(self):
		pass

	def getMaxPercent(self):
		return self.data[self.get_max_position()][0]*100
