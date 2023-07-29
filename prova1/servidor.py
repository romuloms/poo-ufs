## Questão 01

from random import randint

class Servidor:
	
	def __init__(self, nomeServidor, salarioServidor):
		self.__nomeServidor = nomeServidor
		self.__numeroMatricula = randint(1, 10000)
		if salarioServidor >= 0:
			self.__salarioServidor = salarioServidor
		else:
			self.__salarioServidor = 0
	
	def getNomeServidor(self):
		return self.__nomeServidor
	
	def setNomeServidor(self, novoNomeServidor):
		if novoNomeServidor == '':
			print('Nao possivel deixar nome do servidor vazio')
			return
		self.__nomeServidor = novoNomeServidor

	def getSalarioServidor(self):
		return self.__salarioServidor
		
	def setSalarioServidor(self, novoSalarioServidor):
		if novoSalarioServidor < 0:
			print('Nao possivel atribuir valores negativos ao salario')
			return
		else:
			self.__salarioServidor = novoSalarioServidor
	
	def getNumeroMatricula(self):
		return self.__numeroMatricula
	
	def setNumeroMatricula(self, novoNumeroMatricula):
		if novoNumeroMatricula >= 0 and novoNumeroMatricula < 10000:
			self.__numeroMatricula = novoNumeroMatricula
		print('O numero de matricula deve conter no máximo 4 digitos')
	
	def imprimeDadosServidor(self):
		print('Nome: {} | Salario: {} | Numero de Matricula: {}'.format(self.getNomeServidor(), self.getSalarioServidor(), self.getNumeroMatricula()))
		# print(f'nome: {self.getNomeServidor()} | Salario: {self.getSalarioServidor()}')

	def __str__(self):
		representation = 'Nome: {} | Salario: {} | Numero de Matricula: {}'.format(self.getNomeServidor(), self.getSalarioServidor(), self.getNumeroMatricula())
		return representation
