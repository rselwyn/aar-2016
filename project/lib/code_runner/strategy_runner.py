

class StrategyRunner(object):

	def __init__(self, strategy, stop_loss, data):
		self.strategy = strategy
		self.stop_loss = stop_loss
		self.data = data

	def run_strategy(self):
		"""
		Simulates a stock's performance with a buy-signal strategy and a stop-loss
		strategy.
		"""

		has_open_trade = False
		profits = []

		price_at_purchase = None

		# Subtract one because this shouldn't run for the last data point
		for each_day in range(len(self.data)-1):
			current_stock_price = self.data[each_day]
			tomorrow_stock_price = self.data[each_day+1]

			if not has_open_trade:
				# If there isn't an open trade
				if self.strategy.should_buy(current_stock_price, tomorrow_stock_price):
					has_open_trade = True
					price_at_purchase = current_stock_price.get_open()
					print "[SIM] BUY Triggered at {} on day {}.".format(price_at_purchase, current_stock_price.get_date())
			else:
				# If there is an open trade
				self.stop_loss.update(current_stock_price.get_open())

				if self.stop_loss.should_exit():
					has_open_trade = False
					profits.append(current_stock_price.get_open() - price_at_purchase)
					print "[SIM] STOP Triggered at {} on day {}.  Total Profits from Trade: {}.  Overall profits: {}".format(current_stock_price.get_open(), current_stock_price.get_date(), profits[:-1], sum(profits))
					price_at_purchase = None

		return profits
