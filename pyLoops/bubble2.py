valores = [3, 2, 7, 4, 1]
desordenado = True
while desordenado:
    # assumindo que nao encontre mais pares fora de ordem
    desordenado = False
    # buscando elementos fora de ordem
    for i in range(len(valores) - 1):
        if valores[i] > valores[i+1]:
            # invertendo os elementos de ordem
            valores[i], valores[i+1] = valores[i+1], valores[i]
            desordenado = True
            print(valores)