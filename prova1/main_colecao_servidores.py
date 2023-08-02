## Questão 4


from servidor import Servidor
from colecao_servidores import ColecaoServidor


def main():
	##Criação de objetos da classe Servidor:
	servidor = Servidor('itor', 500)
	servidor01 = Servidor('ser01', 500)
	servidor02 = Servidor('ser02', 500)
	servidor03 = Servidor('ser03', 500)
	
	
	## Teste da função de inserir um servidor na colecao
	colecaoServidor = ColecaoServidor()
	colecaoServidor.inserirServidor(servidor)
	colecaoServidor.inserirServidor(servidor01)
	colecaoServidor.inserirServidor(servidor02)
	colecaoServidor.inserirServidor(servidor03)
	
	print('\n\nTeste da função numero de servidores: ')
	print(colecaoServidor.numeroDeServidores())
	
	
	print('Teste da função de imprimir todos os servidores da lista')
	colecaoServidor.listarServidores()

	print('-----------\n\n')
	
	## Teste de remover servidor da coleção
	colecaoServidor.removerServidor(servidor)
	colecaoServidor.removerServidor(servidor01)


	print('Teste da função de numero de servidor na colecao')
	print(colecaoServidor.numeroDeServidores())
	print('\n\n\n----')
	print('Teste da função de imprimir todos os servidores da lista - Após o teste da função de remoção')
	colecaoServidor.listarServidores()




	print('\nTeste da função de verificar um servidor na list------')
	## Verificação do servidor
	servidorExiste = colecaoServidor.verificaServidorNaColecao('itor')
	if servidorExiste == True:
		print('O servidor desejado existe nessa colecao')
	else:
		print('O servidor desejado não existe nessa colecao')

	
main()
