import random


class Notebook: 
    def __init__(self): 
        self.__notes = list()

    def storeNote(self, note): 
        self.__notes.append(note)

    def numberOfNotes(self): 
        return len(self.__notes)
    
    def listNotes(self): 
        for note in self.__notes: print(note)

    def showNote(self, noteNumber): 
        if (noteNumber<0) or (noteNumber>=self.numberOfNotes()): 
            print("Valor invalido") 
        else: 
            print(self.__notes[noteNumber])

    def removeNote(self, note): 
        if note in self.__notes: 
            self.__notes.remove(note) 
        else: 
            print("Nota invalida")

    def hasNotes(self): 
        if len(self.__notes) > 0: 
            return True
        else: 
            return False

    def compareNote(self, note):
        if self.__notes.count(note) != 0:
            return True
        else:
            return False

    def showNoteRandom(self):
        randomNumber = random.randint(0, len(self.__notes)-1)
        print(self.__notes[randomNumber])

    def showMultiNoteRandom(self, notes):
        i = 1
        while i <= notes:
            randomNumber = random.randint(0, len(self.__notes)-1)
            print(self.__notes[randomNumber])
            i += 1

    def printHasNotes(self):
        if self.hasNotes():
            print("Existem notas na lista")
        else:
            print("Lista vazia")
