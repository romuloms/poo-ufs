from CommandWord import CommandWord

class CommandWords:
    def __init__(self):
        self.__validCommands = {}
        for command in CommandWord:
            if command != CommandWord.UNKNOWN:
                self.__validCommands[command.name] = command
    
    def getCommandWord(self, commandWord):
        command = self.__validCommands.get(commandWord)
        if command is not None:
            return command
        else:
            return CommandWord.UNKNOWN
    
    def isCommand(self, command):
        return command in self.__validCommands
    
    def showAll(self):
        for command in self.__validCommands:
            print(command, end=" ")
        print()
