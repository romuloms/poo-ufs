from ponto import Ponto


ponto1 = Ponto()
ponto2 = Ponto(2, 3)

print("--- teste imprime() ---")
ponto1.imprime()
ponto2.imprime()
print("--- teste set() ---")
ponto1.setX(-3)
ponto1.setY(-4)
ponto1.imprime()
print("--- teste get() ---")
print(ponto1.getX())
print(ponto1.getY())

print("--- teste distancia() ---")
dist = ponto1.distanciaPontos(ponto2)
print(dist)