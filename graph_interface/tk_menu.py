from tkinter import *

class MainFrame:
    def __init__(self, parent):
        self.principal = Menu(parent)
        self.arquivo = Menu(self.principal)
        self.arquivo.add_command(label="Abrir")
        self.arquivo.add_command(label="Salvar")
        self.principal.add_cascade(label="Arquivo", menu=self.arquivo)
        self.principal.add_command(label="Ajuda")
        parent.configure(menu=self.principal)
    
root = Tk()
myapp = MainFrame(root)
root.mainloop()