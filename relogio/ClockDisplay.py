from NumberDisplay import NumberDisplay
import math


class ClockDisplay:
    def __init__(self):
        self.__hours = NumberDisplay(9, 24)
        self.__minutes = NumberDisplay(55, 60)

    def timeTick(self, timePassed):
        minutesOverall = self.__minutes.getValue() + timePassed
        if (minutesOverall >= 60):
            self.__hours.increment(math.floor(minutesOverall/60))

        self.__minutes.increment(timePassed)

    def display(self):
        print(f"{self.__hours.displayValue()} : {self.__minutes.displayValue()}")
