class NumberDisplay:
    def __init__(self, limit):
        # value of display, limit of type (h, min, s)
        self.__value = 0
        self.__limit = limit

    def increment(self):
        # adds 1 to the value. when it reaches the limit, goes back to 0
        self.__value = (self.__value + 1) % self.__limit

    def displayValue(self):
        # display string
        if (self.__value < 10):
            return "0" + str(self.__value)
        else:
            return "" + str(self.__value)
        
    def getValue(self):
        # simple return value function
        return self.__value

    def setValue(self, replacementValue):
        # change value to a desired one
        if((replacementValue >= 0) and (replacementValue < self.__limit)):
            self.__value = replacementValue
