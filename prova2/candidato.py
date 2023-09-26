# Aluno: Romulo Menezes de Santana

class Candidato:
    def __init__(self, nome, cpf, rg, email, telefone, pontos):
        self.__nome = "nome"
        self.__cpf = "cpf"
        self.__rg = "rg"
        self.__email = "email"
        self.__telefone = "telefone"
        self.__pontos = 0
        self.setNome(nome)
        self.setCPF(cpf)
        self.setRG(rg)
        self.setEmail(email)
        self.setTelefone(telefone)
        self.setPontos(pontos)

    def getNome(self):
        return self.__nome
    
    def getCPF(self):
        return self.__cpf
    
    def getRG(self):
        return self.__rg
    
    def getEmail(self):
        return self.__email
    
    def getTelefone(self):
        return self.__telefone
    
    def getPontos(self):
        return self.__pontos
    
    def setNome(self, novoNome):
        if type(novoNome) != str:
            raise ValueError("O nome deve ser do tipo string.")
        elif novoNome == "":
            raise ValueError("O nome nao pode ser vazio.")
        else:
            self.__nome = novoNome

    def setCPF(self, novoCPF):
        ## tipo str para nao acabar desconsiderando um primeiro 0 caso fosse do tipo int
        if type(novoCPF) != str:
            raise ValueError("O cpf deve ser do tipo string.")
        elif novoCPF == "":
            raise ValueError("O cpf nao pode ser vazio.")
        else:
            self.__cpf = novoCPF

    def setRG(self, novoRG):
        if type(novoRG) != str:
            raise ValueError("O rg deve ser do tipo string.")
        elif novoRG == "":
            raise ValueError("O rg nao pode ser vazio.")
        else:
            self.__rg = novoRG

    def setEmail(self, novoEmail):
        if type(novoEmail) != str:
            raise ValueError("O email deve ser do tipo string.")
        elif novoEmail == "":
            raise ValueError("O email nao pode ser vazio.")
        else:
            self.__email = novoEmail

    def setTelefone(self, novoTelefone):
        if type(novoTelefone) != str:
            raise ValueError("O telefone deve ser do tipo string.")
        elif novoTelefone == "":
            raise ValueError("O telefone nao pode ser vazio.")
        else:
            self.__telefone = novoTelefone

    def setPontos(self, novoPontos):
        if type(novoPontos) != int:
            raise ValueError("Os pontos devem ser do tipo int.")
        elif novoPontos < 0:
            raise ValueError("Os pontos nao podem ser negativos.")
        else:
            self.__pontos = novoPontos

    def aumentaPontos(self, quantidade):
        if type(quantidade) != int:
            raise ValueError("Os pontos a serem aumentados devem ser do tipo int.")
        elif quantidade <= 0:
            raise ValueError("Os pontos a serem aumentados nao podem ser negativos.")
        else:
            self.__pontos += quantidade

    def strDados(self):
        return f"Nome: {self.__nome}\nCPF: {self.__cpf}\nRG: {self.__rg}\nE-mail: {self.__email}\nTelefone: {self.__telefone}\nPontos: {self.__pontos}"
    
    def imprimeDados(self):
        print("==================================")
        print(self.strDados())