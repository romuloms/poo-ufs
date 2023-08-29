from CommandWords import CommandWords
from Command import Command

class Parser:
    def __init__(self):
        self.commands = CommandWords()
        self.reader = input

    def getCommand(self):
        input_line = input("> ")
        words = input_line.split()
        print(words)

        if len(words) > 0:
            word1 = words[0]
            if len(words) > 1:
                word2 = words[1]
            else:
                word2 = None
        else:
            word1 = None
            word2 = None

        return Command(word1, word2)

    def showCommands(self):
        self.commands.showAll()
