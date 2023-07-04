class Estudante:
    def __init__(self, nome, matricula, creditos=0):
        self.__nome = nome
        self.__matricula = matricula
        self.__creditos = creditos

    def showNome(self):
        print("nome: " + self.__nome)

    def showMatricula(self):
        print("matricula: " + self.__matricula)

    def showCreditos(self):
        print("creditos: " + str(self.__creditos))

    def addCreditos(self, creditos):
        self.__creditos += creditos
