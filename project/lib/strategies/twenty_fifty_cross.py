from trading_strategy import TradingStrategy

class TwentyFiftyMovingAverageCross(TradingStrategy):
    """
    Implementation of a twenty day - fifty day moving average cross.
    """

    def __init__(self):
        pass

    def should_buy(self, first, second):
        if first.get_nth_day_moving_average(20) > first.get_nth_day_moving_average(50):
            # If the 25 day moving average was initially less than the 50 day,
            # then a crossover would cause the 50 to be larger than the 25
            if second.get_nth_day_moving_average(50) > first.get_nth_day_moving_average(20):
                return True
        else:
            # If the 50 day moving average was initially greater than the 25 day average,
            # the crossover would cause 50 to be less

            if second.get_nth_day_moving_average(20) > second.get_nth_day_moving_average(50):
                return True

        # If nothing has happened yet, return False
        return False
