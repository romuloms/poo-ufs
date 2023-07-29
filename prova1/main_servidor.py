## Questão 02

from servidor import Servidor

def main():
	servidor01 = Servidor('itor', -500)
	
	print('Teste dos getters')
	print(servidor01.getNomeServidor())
	print(servidor01.getNumeroMatricula())
	print(servidor01.getSalarioServidor())
	
	print('\n\n\n------')
	
	## Teste dos setters
	servidor01.setSalarioServidor(-1) ## Testa para tentativa de colocar valores negativos ao salario
	print('salario negativo: {}'.format(servidor01.getSalarioServidor()))

	servidor01.setSalarioServidor(100)
	servidor01.setNumeroMatricula(12000) ## Testa para tentativa de colocar um valor maior de 4 digitos no numero de matricula
	servidor01.setNumeroMatricula(-1) ## Testa para tentativa de atribuir um valor negativo a matricula
	print('mat negativa: {}'.format(servidor01.getNumeroMatricula()))

	servidor01.setNumeroMatricula(400)
	servidor01.setNomeServidor('Robson')
	print(servidor01.getNomeServidor())
	servidor01.setNomeServidor('') ## Testa tentativa de atribuir '' ao nome do servidor
	print(f'nome:{servidor01.getNomeServidor()}, blabla')
	
	print('\n\nTeste da função de imprimir todos os atributos e seus respectivos valores')
	servidor01.imprimeDadosServidor()


	print('\n\n\n------')
	print('Testes dos getters')
	print(servidor01.getNomeServidor())
	print(servidor01.getNumeroMatricula())
	print(servidor01.getSalarioServidor())

main()
