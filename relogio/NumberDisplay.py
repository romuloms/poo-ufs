class NumberDisplay:
    def __init__(self, value, limit):
        self.__value = value
        self.__limit = limit

    def increment(self, timePassed):
        self.__value = (self.__value + timePassed) % self.__limit

    def displayValue(self):
        if (self.__value < 10):
            return "0" + str(self.__value)
        else:
            return "" + str(self.__value)
        
    def getValue(self):
        return self.__value
