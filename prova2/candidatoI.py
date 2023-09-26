# Aluno: Romulo Menezes de Santana

from candidato import Candidato


class CandidatoI(Candidato):
    def __init__(self, nome, cpf, rg, email, telefone, pontos, numRANI):
        super().__init__(nome, cpf, rg, email, telefone, pontos)
        self.__numRANI = 0
        self.setNumRANI(numRANI)

    def getNumRANI(self):
        return self.__numRANI
    
    def setNumRANI(self, novoNum):
        if type(novoNum) != int:
            raise ValueError("O numero RANI deve ser do tipo int.")
        elif novoNum < 0:
            raise ValueError("O numero RANI nao pode ser negativo.")
        else:
            self.__numRANI = novoNum

    def imprimeDadosI(self):
        print("==============================")
        print(f"{super().strDados()}\nNumero RANI: {self.__numRANI}")