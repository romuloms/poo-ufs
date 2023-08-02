class Plano:
    def __init__(self):
        self.__pontos = list()

    def inserir(self, ponto):
        self.__pontos.append(ponto)
    
    def remover(self, ponto):
        if self.verificaPonto(ponto):
            self.__pontos.remove(ponto)
            return True
        else:
            return False

    def listar(self):
        contador = 0
        while contador < len(self.__pontos):
            self.__pontos[contador].imprime()
            contador += 1

    def verificaPonto(self, p):
        for ponto in self.__pontos:
            if ponto == p:
                return True
        return False