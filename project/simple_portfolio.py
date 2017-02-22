from __future__ import division
# from lib.plotting.plot_util import StockNumberBasedPlot
from lib.data_collection.pandas_collector import PandasBasedDataReader
from lib.util.statistics import MovingAverageCalculator

from lib.code_runner.strategy_runner import StrategyRunner
from lib.stop_losses.implementation import *
from lib.strategies.twenty_fifty_cross import TwentyFiftyMovingAverageCross

import datetime

start = datetime.datetime(2008,10,8)
end = datetime.datetime(2013,2,10)

companies = ["AAPL", "GOOG", "FB", "JPM", "VZ", "JNJ"]

reader = [PandasBasedDataReader(start,end, i) for i in companies]
data = [i.get_data(calculate_moving_averages=[20,50]) for i in reader]


strategy = TwentyFiftyMovingAverageCross()

csvOut = open("research.csv","w")

# collected_data = []

for i in range(1,10000, 5):
	total_cash = 0

	for company in data:
		value = i/10000
		stop_loss = LinearlyTrailingStopLoss(value)
		runner = StrategyRunner(strategy, stop_loss, company)
		total = sum(runner.run_strategy())
		total_cash += total

	csvOut.write(str(value) + ", " + str(total_cash) +'\n')


# print (sorted(collected_data, key=lambda i: i[1], reverse=True)[0])

csvOut.close()
