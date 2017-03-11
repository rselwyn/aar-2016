from collections import defaultdict

class Portfolio(object):

	def __init__(self, name):
		self.name = name

		# Holds {Company: Percent: Return}
		self.data = defaultdict(dict)
		self.stats = defaultdict(dict)

	def add_data(self, company, percent, point):
		self.data[str(company)][str(percent)] = point

	def get_data(self, company, percent):
		return self.data[str(company)][str(percent)]

	def print_all_data(self):
		print dict(self.data)

	def print_stats(self):
		print dict(self.stats)

	def update_stats(self, percent, stat, value):
		self.stats[str(percent)][stat] = value

