from Conta import Conta

conta1 = Conta("Robson", 1234500)

conta1.deposito(1000)
conta1.imprimeConta()

def tentarSaque(valor):
    sucesso = False
    tentativas = 0
    while (not sucesso) and (tentativas < 3):
        try:
            conta1.saque(valor)
            sucesso = True
        except ValueError as erro:
            print(erro)
            tentativas += 1
    if not sucesso:
        print("Nao foi possivel realizar o saque")
        tentativas = 0

def tentarDeposito(valor):
    sucesso = False
    tentativas = 0
    while (not sucesso) and (tentativas < 3):
        try:
            conta1.deposito(valor)
            sucesso = True
        except ValueError as erro:
            print(erro)
            tentativas += 1
    if not sucesso:
        print("Nao foi possivel realizar o deposito")
        tentativas = 0

tentarSaque(1550)
tentarDeposito(30)

try:
    conta1.setNomeCorrentista("Lau")
    conta1.setNumeroConta("44")
except ValueError as erro:
    print(erro)

conta1.imprimeConta()