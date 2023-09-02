class Command:
    def __init__(self, commandWord, secondWord):
        self.__commandWord = commandWord
        self.__secondWord = secondWord

    def getCommandWord(self):
        return self.__commandWord
    
    def getSecondWord(self):
        return self.__secondWord
    
    def isUnknown(self):
        return self.__commandWord is None
    
    def hasSecondWord(self):
        return self.__secondWord is not None
    
