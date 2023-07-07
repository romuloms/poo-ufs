class NumberDisplay:
    def __init__(self, limit):
        # value of display, limit of type (h, min, s)
        self._value = 0
        self._limit = limit

    def increment(self):
        # adds 1 to the value. when it reaches the limit, goes back to 0
        self._value = (self._value + 1) % self._limit

    def displayValue(self):
        # display string
        if (self._value < 10):
            return "0" + str(self._value)
        else:
            return "" + str(self._value)
        
    def getValue(self):
        # simple return value function
        return self._value

    def setValue(self, replacementValue):
        # change value to a desired one
        if((replacementValue >= 0) and (replacementValue < self._limit)):
            self._value = replacementValue
