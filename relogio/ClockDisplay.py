from NumberDisplay import NumberDisplay


class ClockDisplay:
    def __init__(self, hours, minutes, seconds):
        self.__hours = NumberDisplay(24)
        self.__minutes = NumberDisplay(60)
        self.__seconds = NumberDisplay(60)
        self.__displayString = ""
        self.setTime(hours, minutes, seconds)
        self.updateDisplay()

    def timeTick(self):
        self.__seconds.increment()

        if (self.__seconds.getValue() == 0):
            self.__minutes.increment()
            if (self.__minutes.getValue() == 0):
                self.__hours.increment()
        
        self.updateDisplay()
        
    def updateDisplay(self):
        self.__displayString = str(self.__hours.displayValue()) + ":" + str(self.__minutes.displayValue()) + ":" + str(self.__seconds.displayValue())

    def setTime(self, hour, minute, second):
        self.__hours.setValue(hour)
        self.__minutes.setValue(minute)
        self.__seconds.setValue(second)
        self.updateDisplay()

    def getTime(self):
        print(self.__displayString)

    def runClock(self, timeInSeconds):
        for i in range(timeInSeconds):
            self.timeTick()
            self.getTime()
