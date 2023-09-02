class CommandWords:
    def __init__(self):
        # a constant tuple that holds all valid command words
        self.__validCommands = ("go", "quit", "help")

    def isCommand(self, aString):
        if(aString in self.__validCommands):
            return True
        else:
            # the string was not found in the commands
            return False