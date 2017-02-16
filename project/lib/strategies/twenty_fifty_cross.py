from trading_strategy import TradingStrategy

class TwentyFiftyMovingAverageCross(TradingStrategy):
    """
    Implementation of a twenty day - fifty day moving average cross.
    """

    def __init__(self):
        pass

    def should_buy(self, first, second):
        if first.get_nth_day_moving_average(20) < first.get_nth_day_moving_average(50):
            # If the 20 day moving average was initially less than the 50 day,
            # then a crossover would cause the 50 to be less than the 20
            if second.get_nth_day_moving_average(20) > first.get_nth_day_moving_average(50):
                return True

        return False

    def should_sell(self, first, second):
        if first.get_nth_day_moving_average(50) < first.get_nth_day_moving_average(20):
            # If the 20 day moving average was initially less than the 50 day,
            # then a crossover would cause the 50 to be less than the 20
            if second.get_nth_day_moving_average(50) > first.get_nth_day_moving_average(20):
                return True

        return False