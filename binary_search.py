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


listaDeEntrada = input("digite os elementos separados por espaco: ")
lista = [int(elemento) for elemento in listaDeEntrada.split()]

elementoDeEntrada = input("digite o elemento que deseja buscar na lista: ")
elementoInteiro = int(elementoDeEntrada)

print(pesquisaBinaria(lista, elementoInteiro))
