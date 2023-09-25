from CadastroProduto import CadastroProduto
from Produto import Produto
from Computador import Computador


listaDeProdutos = CadastroProduto()
miojo = Produto("Superprocessado", "123abc", "Macarrao instantaneo")
pc = Computador("elet", "123a", "pc", "de mesa", 100, True)
note = Computador("elet", "123b", "pc", "de mesa", 0, False)

listaDeProdutos.insereProduto(miojo)
listaDeProdutos.insereProduto(pc)
listaDeProdutos.insereProduto(note)
listaDeProdutos.imprimeComputadores()