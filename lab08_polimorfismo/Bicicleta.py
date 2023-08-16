from Veiculo import Veiculo


class Bicicleta(Veiculo):
    def __init__(self, placaVeiculo, fabricanteVeiculo, numeroRodas, tipoVeiculo, numeroMarchas):
        super().__init__(placaVeiculo, fabricanteVeiculo, numeroRodas, tipoVeiculo)
        self.__numeroMarchas = numeroMarchas
        self.setTipoVeiculo("Bicicleta")

    def getNumeroMarchas(self):
        return self.__numeroMarchas
    
    def setNumeroMarchas(self, num):
        if num <= 0:
            print("Valor invalido")
        else:
            self.__numeroMarchas = num

    def imprime(self):
        print(f"{super().imprime()}\nNumero de marchas: {str(self.__numeroMarchas)}\n-----------------")