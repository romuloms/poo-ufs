from notebook import Notebook


myNotebook = Notebook()

note1 = input("Digite a primeira nota: ")
note2 = input("Digite a segunda nota: ")
note3 = input("Digite a terceira nota: ")

myNotebook.storeNote(note1)
myNotebook.storeNote(note2)
myNotebook.storeNote(note3)

print("Numero de notas: ", myNotebook.numberOfNotes())
print("Notas: ")
myNotebook.listNotes()

searchedNote = int(input("Digite o indice da nota que quer encontrar: "))
myNotebook.showNote(searchedNote)

removedNote = input("Digite a nota que quer remover: ")
myNotebook.removeNote(removedNote)

print("Numero de notas: ", myNotebook.numberOfNotes())

print("metodo showNoteRandom:")
myNotebook.showNoteRandom()

print("metodo showMultiNoteRandom:")
myNotebook.showMultiNoteRandom(3)

myNotebook.printHasNotes()