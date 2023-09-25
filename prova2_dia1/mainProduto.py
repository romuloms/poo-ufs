from Produto import Produto

miojo = Produto("Superprocessado", "123abc", "Macarrao instantaneo")

miojo.imprimeProduto()
sucesso = False

try:
    miojo.setCodigo("")
    sucesso = True
except ValueError as erro:
    print(erro)

if sucesso:
    miojo.imprimeProduto()