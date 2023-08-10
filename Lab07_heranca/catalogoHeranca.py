from cdHeranca import CD
from dvdHeranca import DVD


class Catalogo:
    def __init__(self):
        self.__itens = list()

    def inserirItem(self, item):
        self.__itens.append(item)

    def removerItem(self, item):
        self.__itens.remove(item)

    def listarItens(self):
        for item in self.__itens:
            if (isinstance(item, CD)):
                print("------------")
                print("Tipo: CD")
                item.imprimirCD()
            if (isinstance(item, DVD)):
                print("------------")
                print("Tipo: DVD")
                item.imprimirDVD()

    def localizarItem(self, titulo):
        for item in self.__itens:
            if(titulo == item.getTitulo()):
                if (isinstance(item, CD)):
                    item.imprimirCD()
                if (isinstance(item, DVD)):
                    item.imprimirDVD()
