
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

		last_stop_loss_price = None

		# We don't want the first day.
		for each_day in range(1, len(self.data)):
			yesterday_stock_price = self.data[each_day-1]
			today_stock_price = self.data[each_day]

			if not has_open_trade:
				# If there isn't an open trade
				if self.strategy.should_buy(yesterday_stock_price, today_stock_price):
					has_open_trade = True
					price_at_purchase = today_stock_price.get_open()
					self.stop_loss.set_stop_loss_base_price(today_stock_price.get_open())
					print "[SIM] BUY Triggered at {} on day {}.".format(price_at_purchase, today_stock_price.get_date())
					print "[SIM] STOP Set at {}.".format(self.stop_loss.get_current_stop())
					last_stop_loss_price = self.stop_loss.get_current_stop()
			else:
				# If there is an open trade
				self.stop_loss.update(today_stock_price.get_open())

				if last_stop_loss_price != self.stop_loss.get_current_stop():
					last_stop_loss_price = self.stop_loss.get_current_stop()
					print "[SIM] STOP Updated to {}.".format(last_stop_loss_price)

				if self.stop_loss.should_exit():
					has_open_trade = False
					profits.append(today_stock_price.get_open() - price_at_purchase)
					print "[SIM] STOP Triggered at {} on day {}.  Total Profits from Trade: {}.  Overall profits: {}".format(today_stock_price.get_open(), today_stock_price.get_date(), profits[-1], sum(profits))
					price_at_purchase = None

		return profits
