from Produto import Produto


class Computador(Produto):
    def __init__(self, tipo, codigo, descricao, modelo, disponibilidade, temNoEstoque):
        super().__init__(tipo, codigo, descricao)
        self.__modelo = modelo
        self.__disponibilidade = 0
        self.__temNoEstoque = False
        self.setTipo("Eletronicos")
        self.setDisponibilidade(disponibilidade)
        self.setTemNoEstoque(temNoEstoque)

    def setModelo(self, novoModelo):
        if novoModelo == "":
            raise ValueError("O modelo do computador nao pode ser vazio")
        elif type(novoModelo) != str:
            raise ValueError("O modelo do computador deve ser string")
        else:
            self.__modelo = novoModelo
    
    def setDisponibilidade(self, valor):
        if type(valor) != int:
            raise ValueError("A quantia em estoque deve ser do tipo inteiro")
        elif valor < 0:
            raise ValueError("A quantia em estoque deve ser maior ou igual a zero")
        else:
            self.__disponibilidade = valor

    def aumentaEstoque(self, valor):
        if type(valor) != int:
            raise ValueError("O valor a ser aumentado deve ser do tipo inteiro")
        elif valor <= 0:
            raise ValueError("O valor a ser aumentado deve ser maior do que zero")
        else:
            self.__disponibilidade += valor

    def diminuiEstoque(self, valor):
        if type(valor) != int:
            raise ValueError("O valor a ser reduzido deve ser do tipo inteiro")
        elif valor <= 0:
            raise ValueError("O valor a ser aumentado deve ser maior do que zero")
        elif (self.__disponibilidade - valor) < 0:
            raise ValueError("O valor a ser reduzido nao pode ser maior do que a disponibilidade atual em estoque")
        else:
            self.__disponibilidade -= valor
            if self.__disponibilidade == 0:
                self.setTemNoEstoque(False)
    
    def setTemNoEstoque(self, novoBool):
        if type(novoBool) != bool:
            raise ValueError("O tipo da flag deve ser booleano")
        elif (self.__disponibilidade > 0) and novoBool != True:
            raise ValueError("Existe estoque")
        elif (self.__disponibilidade < 0) and novoBool != False:
            raise ValueError("Nao existe estoque")
        else:
            self.__temNoEstoque = novoBool

    def getModelo(self):
        return self.__modelo
    
    def getDisponibilidade(self):
        return self.__disponibilidade
    
    def getTemNoEstoque(self):
        return self.__temNoEstoque
    
    def imprimePC(self):
        print(f"{super().imprimeProduto()}\nModelo do computador: {self.getModelo()}\nDisponibilidade: {self.__disponibilidade}\nTem no estoque: {self.getTemNoEstoque()}")