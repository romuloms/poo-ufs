from CommandWords import CommandWords
from Command import Command

class Parser: 
    # create a parser to read commands from the terminal
    def __init__(self): 
        self.__commands = CommandWords() # holds all valid command words

    # return user command
    def getCommand(self):
        word1 = None
        word2 = None

        inputLine = input("> ").split()

        # find up to two words on the line
        if(len(inputLine) >= 1):
            word1 = inputLine[0]
        if(len(inputLine) == 2):
            word2 = inputLine[1]

        # check whether this word is known. if so, create a command
        # if not, create a null command (for unknown command).
        if(self.__commands.isCommand(word1)):
            return Command(word1, word2)

        else:
            return Command(None, word2)
