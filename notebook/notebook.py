class Notebook:
    def __init__(self):
        self.__notes = list()

    def storeNote(self, note):
        self.__notes.append(note)

    def numberOfNotes(self):
        return len(self.__notes)
    
    def listNotes(self):
        for note in self.__notes:
            print(note)
    
    def showNote(self, noteNumber):
        if (noteNumber < 0) or (noteNumber >= self.numberOfNotes()):
            print("Valor invalido.")
        else:
            print(self.__notes[noteNumber])
    
    def removeNote(self, note):
        if note in self.__notes:
            self.__notes.remove(note)
        else:
            print("Nota invalida.")
