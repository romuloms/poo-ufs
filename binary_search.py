from quicksort import quicksort


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

    return baixo    # returns the position item should be if it is not in list


# listaDeEntrada = input("digite os elementos separados por espaco: ")
# lista = [int(elemento) for elemento in listaDeEntrada.split()]
# listaOrdenada = quicksort(lista)

# elementoDeEntrada = input("digite o elemento que deseja buscar na lista: ")
# elementoInteiro = int(elementoDeEntrada)

# print(listaOrdenada)
# print(pesquisaBinaria(listaOrdenada, elementoInteiro))

lista = [0, 2, 4]
print(pesquisaBinaria(lista, 1))
