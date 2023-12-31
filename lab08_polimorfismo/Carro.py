from Veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, placaVeiculo, fabricanteVeiculo, numeroRodas, tipoVeiculo, numeroPortas):
        super().__init__(placaVeiculo, fabricanteVeiculo, numeroRodas, tipoVeiculo)
        self.__numeroPortas = numeroPortas
        self.setTipoVeiculo("Carro")

    def getNumeroPortas(self):
        return self.__numeroPortas
    
    def setNumeroPortas(self, num):
        if num > 0:
            self.__numeroPortas = num
        else:
            print("Valor invalido")

    def imprime(self):
        # print(f"{super().imprime()}\nNumero portas: {str(self.__numeroPortas)}\n-----------------")
        print("{}\nNumero portas: {}\n-----------------".format(super().imprime(), str(self.__numeroPortas)))