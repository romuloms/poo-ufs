from Produto import Produto
from Computador import Computador


class CadastroProduto:
    def __init__(self):
        self.__produtos = list()
    
    def insereProduto(self, produto):
        if isinstance(produto, Produto):
            self.__produtos.append(produto)
        else:
            print("O argumento passado deve ser do tipo Produto")
    
    # def removeProduto(self, produto):
    #     if isinstance(produto, Produto):
    #         self.__produtos.remove(produto)
    #     else:
    #         print("O argumento passado deve ser do tipo Produto")

    def imprimeComputadores(self):
        for computador in self.__produtos:
            if isinstance(computador, Computador):
                computador.imprimePC()