from NumberDisplay import NumberDisplay


class ClockDisplay:
    def __init__(self, hours, minutes, seconds):
        # instance each value type with their limits
        # set the time to a starting one of your wanting
        # update the display string
        self.__hours = NumberDisplay(24)
        self.__minutes = NumberDisplay(60)
        self.__seconds = NumberDisplay(60)
        self.__displayString = ""
        self.setTime(hours, minutes, seconds)
        self.updateStrDisplay()

    def updateStrDisplay(self):
        # function to save the display on a string
        self.__displayString = str(self.__hours.displayValue()) + ":" + str(self.__minutes.displayValue()) + ":" + str(self.__seconds.displayValue())
    
    def timeTick(self):
        # adds 1 second to the seconds value
        self.__seconds.increment()

        if (self.__seconds.getValue() == 0):
            # adds 1 minute to the minute value if it has passed 60 seconds
            self.__minutes.increment()
            if (self.__minutes.getValue() == 0):
                # adds 1 hour to the hour value if it has passed 60 minutes
                self.__hours.increment()
        
        # update the display string
        self.updateStrDisplay()

    def setTime(self, hour, minute, second):
        # setting the starting time
        self.__hours.setValue(hour)
        self.__minutes.setValue(minute)
        self.__seconds.setValue(second)
        # update the display string
        self.updateStrDisplay()

    def showTime(self):
        # function to show current display on terminal
        print(self.__displayString)

    def runClock(self, timeInSeconds):
        # loop function to increment the time and show every second passing on terminal
        for i in range(timeInSeconds):
            self.timeTick()
            self.showTime()
