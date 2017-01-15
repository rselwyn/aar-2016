# aar-2016
A repository for Robbie Selwyn and Ayush Gupta's AAR project at Palo Alto High School.

##code-runner
###strategy_runner.py
Runs strategy.

##data_collection
###pandas_collector.py
Gets stock data using pandas data reader.

##models
###stock_model.py
Class StockOHCLV, get info. Class BasicStock, get info.

###stock.py
Abstract class, extended by all stock model data types.

##plotting
###plot_util.py
Class for plotting stock history, using matplotlib.

##stop_losses
###implementation.py
Three types of stop losses: hard, linearly trailing, non-linearly trailing.
Non-linearly trailing stops still need to be implemented.

###stop_loss.py
Abstract class, extended by all stop loss objects.

##strategies
###trading_strategy.py
Abstract class, extended by all trading strategy types.

##util
###statistics.py
Ratio Calculator: Sharpe ratio, Sortino ratio.
Mathematical Calculator: standard deviation, mean.
Moving Average Calculator: get moving average over days, bind moving average to points.
