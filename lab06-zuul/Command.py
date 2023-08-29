from CommandWord import CommandWord

class Command:
    def __init__(self, commandWord, secondWord):
        self.__commandWord = CommandWord(commandWord)
        self.__secondWord = secondWord

    def getCommandWord(self):
        return self.__commandWord
    
    def getSecondWord(self):
        return self.__secondWord
    
    def isUnknown(self):
        return self.__commandWord == CommandWord.UNKNOWN
    
    def hasSecondWord(self):
        return self.__secondWord is not None
    
