from __future__ import division
from lib.plotting.plot_util import StockNumberBasedPlot
from lib.data_collection.pandas_collector import PandasBasedDataReader
from lib.util.statistics import MovingAverageCalculator

from lib.code_runner.strategy_runner import StrategyRunner
from lib.stop_losses.implementation import *
from lib.strategies.twenty_fifty_cross import TwentyFiftyMovingAverageCross

from lib.code_runner.graphoptimizer import GraphOptimizer

import datetime

start = datetime.datetime(2010,1,1)
end = datetime.datetime(2013,4,11)

reader = PandasBasedDataReader(start,end, "VOO")

data = reader.get_data(calculate_moving_averages=[20,50])
strategy = TwentyFiftyMovingAverageCross()

csvOut = open("research.csv","w")

collected_data = []

for i in range(200,10000, 5):

	value = i/10000
	stop_loss = LinearlyTrailingStopLoss(value)
	runner = StrategyRunner(strategy, stop_loss, data)
	total,stops = runner.run_strategy()
	total = sum(total)
	collected_data.append([value, total])

	csvOut.write(str(value) + ", " + str(total) + ", " + str(stops) +"\n")

# print (sorted(collected_data, key=lambda i: i[1], reverse=True)[0])

csvOut.close()

# print collected_data
graph = GraphOptimizer(collected_data)

max_no_strat = data[-1].get_open() - data[0].get_open()

print "STATISTICS: "
print "NINETY PERCENT DISTANCE: " + str(graph.getNinetyPercentDistance())
print "MAX: " + str(graph.getAbsoluteMax())
print "STOP LOSS PERCENT: "  + str(graph.getMaxPercent())
print "MAX NO STRATEGY: " + str(max_no_strat)
print "EXTRA PROFIT PERCENTAGE: " + str(((graph.getAbsoluteMax()-max_no_strat) / max_no_strat) * 100)

days = [i.get_date() for i in data]

graph = StockNumberBasedPlot("Graph of TSLA")

graph.set_axes("Time","Price")
graph.plot_data(data)

graph.plot_numbers_on_day(days,[i.get_nth_day_moving_average(20) for i in data])

graph.plot_numbers_on_day(days, [i.get_nth_day_moving_average(50) for i in data])
graph.show()
