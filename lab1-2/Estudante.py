class Estudante:
    def __init__(self, nome, matricula, creditos=0):
        self.__nome = nome
        self.__matricula = matricula
        self.__creditos = creditos

    def getNome(self):
        print("nome: " + self.__nome)

    def getMatricula(self):
        print("matricula: " + self.__matricula)

    def getCreditos(self):
        print("creditos: " + str(self.__creditos))

    def addCreditos(self, creditos):
        self.__creditos += creditos
