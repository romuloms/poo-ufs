class Produto:
    def __init__(self, tipo, codigo, descricao):
        self.__tipo = tipo
        self.__codigo = codigo
        self.__descricao = descricao

    def setTipo(self, novoTipo):
        if novoTipo == "":
            raise ValueError("O tipo do produto nao pode ser vazio")
        elif type(novoTipo) != str:
            raise ValueError("O tipo do produto deve ser string")
        else:
            self.__tipo = novoTipo
    
    def setCodigo(self, novoCodigo):
        if novoCodigo == "":
            raise ValueError("O codigo nao pode ser vazio")
        elif type(novoCodigo) != str:
            raise ValueError("O codigo deve ser string")
        else:
            self.__codigo = novoCodigo

    def setDescricao(self, novaDescricao):
        if novaDescricao == "":
            raise ValueError("A descricao nao pode ser vazia")
        elif type(novaDescricao) != str:
            raise ValueError("A descricao deve ser string")
        else:
            self.__descricao = novaDescricao

    def getTipo(self):
        return self.__tipo

    def getCodigo(self):
        return self.__codigo
    
    def getDescricao(self):
        return self.__descricao
    
    def imprimeProduto(self):
        print("=======================================")
        return f"Tipo do produto: {self.__tipo}\nCodigo do produto: {self.__codigo}\nDescricao do produto: {self.__descricao}"
