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

reader = PandasBasedDataReader(start,end, "AAPL")

data = reader.get_data(calculate_moving_averages=[20,50])
strategy = TwentyFiftyMovingAverageCross()

csvOut = open("research.csv","w")

collected_data = []

for i in range(1,10000, 5):
	
	value = i/10000
	stop_loss = LinearlyTrailingStopLoss(value*data[0].get_open())
	runner = StrategyRunner(strategy, stop_loss, data)
	total = sum(runner.run_strategy())
	collected_data.append([value, total])

	csvOut.write(str(value) + ", " + str(total) +'\n')

print (sorted(collected_data, key=lambda i: i[1], reverse=True)[0])

csvOut.close()
