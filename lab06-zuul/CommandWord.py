from enum import Enum

class CommandWord(Enum):
    GO = "go"
    QUIT = "quit"
    HELP = "help"
    UNKNOWN = "?"

    def __init__(self, commandString):
        self.commandString = commandString

    def __str__(self):
        return self.commandString
    
# if __name__ == "__main__":
#     cm = CommandWord("go")
#     print(cm)