class NumberDisplay:
    def __init__(self, limit):
        self.__value = 0
        self.__limit = limit

    def increment(self):
        self.__value = (self.__value + 1) % self.__limit

    def displayValue(self):
        if (self.__value < 10):
            return "0" + str(self.__value)
        else:
            return "" + str(self.__value)
        
    def getValue(self):
        return self.__value

    def setValue(self, replacementValue):
        if((replacementValue >= 0) and (replacementValue < self.__limit)):
            self.__value = replacementValue
