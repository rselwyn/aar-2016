from __future__ import division
# from lib.plotting.plot_util import StockNumberBasedPlot
from lib.data_collection.pandas_collector import PandasBasedDataReader
from lib.util.statistics import MovingAverageCalculator
from lib.util.statistics import RatioCalculator

from lib.code_runner.strategy_runner import StrategyRunner
from lib.stop_losses.implementation import *
from lib.strategies.twenty_fifty_cross import TwentyFiftyMovingAverageCross
from lib.models.portfolio import Portfolio

import datetime

start = datetime.datetime(2010,1,1)
end = datetime.datetime(2013,2,10)

f = open("portfolio.txt", "r")
companies = [i.strip("\n") for i in f.readlines()]
f.close()

return_holder = Portfolio("Optimized Portfolio")

total_start_value = 0
total_end_value = 0

stop_value = [i/10000 for i in range(200,5000,5)]
for company in companies:

	reader = PandasBasedDataReader(start,end, company)

	# Get the data and create the strategy
	data = reader.get_data(calculate_moving_averages=[20,50])
	strategy = TwentyFiftyMovingAverageCross()

	total_start_value += data[0].get_open()
	total_end_value += data[-1].get_open()

	print company
	print data[0].get_open(), data[-1].get_open()

	for k in stop_value:
		stop_loss = LinearlyTrailingStopLoss(k)
		runner = StrategyRunner(strategy, stop_loss, data)
		total,stops = runner.run_strategy()
		total = sum(total)
		return_holder.add_data(company, str(k), str(total))

# After the above loops finish running, all the data has been loaded

full_sharpe = []

full_results = open("results_portfolio.csv", "w")

# For each Different Stop Placement, Calculate the stats
for i in stop_value:
	returns = [float(return_holder.get_data(comp, i)) for comp in companies]
	total = sum(returns)
	sortino = RatioCalculator.get_sortino_ratio(returns)
	sharpe = RatioCalculator.get_sharpe_ratio(returns)
	return_holder.update_stats(str(i),"Total", total)
	return_holder.update_stats(str(i), "Sortino", sortino)
	return_holder.update_stats(str(i), "Sharpe", sharpe)
	full_sharpe.append([i, sharpe, total])
	full_results.write(str(i) + "," + str(total) + ", " + str(sharpe) + "\n")

print "FULL RESULTS FOR PORTFOLIO: "
print "MOST RETURNS WERE WITH STOP PERCENT " + str(sorted(full_sharpe, key=lambda i: i[2], reverse=True)[0])
print "HIGHEST SHARPE WAS WITH STOP PERCENT " + str(sorted(full_sharpe, key=lambda i: i[1], reverse=True)[0])
print "NO STRATEGY RESULT OF: " + str(total_end_value - total_start_value)

full_results.close()
# return_holder.print_stats()
