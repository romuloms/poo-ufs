class Estudante:
    def __init__(self, nome, matricula, creditos=0):
        self.__nome = nome
        self.__matricula = matricula
        self.__creditos = creditos

    def getNome(self):
        print(self.__nome)

    def getMatricula(self):
        print(self.__matricula)

    def getCreditos(self):
        print(self.__creditos)
