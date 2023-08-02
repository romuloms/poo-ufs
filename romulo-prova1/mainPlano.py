from ponto import Ponto
from plano import Plano


plano1 = Plano()
ponto1 = Ponto(-3, -4)
ponto2 = Ponto(2, 5)

tecX = int(input("Digite o valor de X para o ponto3: "))
tecY = int(input("Digite o valor de Y para o ponto3: "))

ponto3 = Ponto(tecX, tecY)

print("--- teste inserir() ---")
plano1.inserir(ponto1)
plano1.inserir(ponto2)
plano1.inserir(ponto3)

print("--- teste listar() ---")
plano1.listar()

print("--- teste verificaPonto() ---")
verifica = plano1.verificaPonto(ponto3)
if verifica:
    print("o ponto 3 esta na lista")
else:
    print("o ponto 3 nao esta na lista")

print("--- teste remover() ---")
rem = plano1.remover(ponto2)
rem2 = plano1.remover(ponto2)
if rem:
    print("ponto removido")
else:
    print("o ponto nao esta na lista")

if rem2:
    print("ponto removido")
else:
    print("o ponto nao esta na lista")