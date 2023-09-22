from tkinter import *

class MainFrame:
    def __init__(self, parent):
        self.principal = Menu(root)
        self.arquivo = Menu(self.principal)
        self.arquivo.add_command(label="Abrir", command=self.abrir)
        self.arquivo.add_command(label="Salvar", command=self.salvar)
        self.principal.add_cascade(label="Arquivo", menu=self.arquivo)
        self.principal.add_command(label="Ajuda", command=self.ajuda)
        parent.configure(menu=self.principal)

    def abrir(self):
        print("abrir")
    
    def salvar(self):
        print("salvar")
    
    def ajuda(self):
        print("ajuda")

root = Tk()
app = MainFrame(root)
root.mainloop()