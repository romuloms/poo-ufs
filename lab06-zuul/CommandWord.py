from enum import Enum

class CommandWord(Enum):
    GO = "go"
    QUIT = "quit"
    HELP = "help"
    UNKNOWN = "?"

    def __init__(self, commandString):
        self.__commandString = commandString

    def __str__(self):
        return self.__commandString
    