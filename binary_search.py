def pesquisaBinaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = int((baixo + alto) / 2)
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None


minhalista = [2, 3, 5, 10, 15, 20, 23, 50, 85, 98, 100]

print(pesquisaBinaria(minhalista, 20))
