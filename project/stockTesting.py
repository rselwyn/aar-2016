from lib.plotting.plot_util import StockNumberBasedPlot
from lib.data_collection.pandas_collector import PandasBasedDataReader
from lib.util.statistics import MovingAverageCalculator

from lib.code_runner.strategy_runner import StrategyRunner
from lib.stop_losses.implementation import *
from lib.strategies.twenty_fifty_cross import TwentyFiftyMovingAverageCross

import datetime

start = datetime.datetime(2011,10,8)
end = datetime.datetime(2013,2,10)

reader = PandasBasedDataReader(start,end, "AAPL")

data = reader.get_data(calculate_moving_averages=[20,50])

stop_loss = LinearlyTrailingStopLoss(10)
strategy = TwentyFiftyMovingAverageCross()


runner = StrategyRunner(strategy, stop_loss, data)
print runner.run_strategy()

days = [i.get_date() for i in data]

graph = StockNumberBasedPlot("Graph of AAPL")

graph.set_axes("Time","Price")
graph.plot_data(data)

graph.plot_numbers_on_day(days,[i.get_nth_day_moving_average(20) for i in data])

graph.plot_numbers_on_day(days, [i.get_nth_day_moving_average(50) for i in data])
graph.show()
