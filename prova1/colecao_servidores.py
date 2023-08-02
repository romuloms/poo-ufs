## Questão 3


# from servidor import Servidor

class ColecaoServidor:
	
	def __init__(self):
		self.__servidores = list()

	def inserirServidor(self, novoServidor):
		self.__servidores.append(novoServidor)
	
	def removerServidor(self, servidorDesejado):
		self.__servidores.remove(servidorDesejado)
	
	def numeroDeServidores(self):
		return len(self.__servidores)
		
	def listarServidores(self):
		cont = 0
		while(cont < self.numeroDeServidores()):
			print(self.__servidores[cont])
			cont += 1
	
	## Função que informa se um dado servidor (através do nome) está na coleção ou nao
	def verificaServidorNaColecao(self, nomeServidor):
		for servidor in self.__servidores:
			if nomeServidor == servidor.getNomeServidor():
				return True
		return False		
