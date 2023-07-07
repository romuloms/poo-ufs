from NumberDisplay import NumberDisplay


class ClockDisplay:
    def __init__(self, hours, minutes, seconds):
        # instance each value type with their limits
        # set the time to a starting one of your wanting
        # update the display string
        self._hours = NumberDisplay(24)
        self._minutes = NumberDisplay(60)
        self._seconds = NumberDisplay(60)
        self._displayString = ""
        self.setTime(hours, minutes, seconds)

    def _updateStrDisplay(self):
        # function to save the display on a string
        self._displayString = str(self._hours.displayValue()) + ":" + str(self._minutes.displayValue()) + ":" + str(self._seconds.displayValue())
    
    def timeTick(self):
        # adds 1 second to the seconds value
        self._seconds.increment()

        if (self._seconds.getValue() == 0):
            # adds 1 minute to the minute value if it has passed 60 seconds
            self._minutes.increment()
            if (self._minutes.getValue() == 0):
                # adds 1 hour to the hour value if it has passed 60 minutes
                self._hours.increment()
        
        # update the display string
        self._updateStrDisplay()

    def setTime(self, hour, minute, second):
        # setting the starting time
        self._hours.setValue(hour)
        self._minutes.setValue(minute)
        self._seconds.setValue(second)
        # update the display string
        self._updateStrDisplay()

    def showTime(self):
        # function to show current display on terminal
        print(self._displayString)

    def runClock(self, timeInSeconds):
        # loop function to increment the time and show every second passing on terminal
        for i in range(timeInSeconds):
            self.timeTick()
            self.showTime()
