from Veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, placaVeiculo, fabricanteVeiculo, numeroRodas, tipoVeiculo, cilindrada):
        super().__init__(placaVeiculo, fabricanteVeiculo, numeroRodas, tipoVeiculo)
        self.__cilindrada = cilindrada
        self.setTipoVeiculo("Moto")

    def getCilindrada(self):
        return self.__cilindrada
    
    def setCilindrada(self, num):
        if num <= 0:
            print("Valor invalido")
        else:
            self.__cilindrada = num

    def imprime(self):
        print(f"{super().imprime()}\nCilindradas: {str(self.__cilindrada)}\n-----------------")