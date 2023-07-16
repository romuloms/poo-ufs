def bubblesort(elements):
    swapped = False
    # obs: range(start, stop, step)
    # o loop comeca no ultimo indice e vai diminuindo 1 ate chegar no indice 0
    for n in range(len(elements)-1, 0, -1):
        # se len(x)==7, n: 6, 5, 4, 3, 2, 1
        for i in range(n):
            # i comeca em 0 e vai ate n-1
            if elements[i] > elements[i+1]:
                # troca os elementos de lugar se o elemento for maior que seu sucessor
                swapped = True
                elements[i], elements[i+1] = elements[i+1], elements[i]

        if not swapped:
            # sai da funcao se nao aconteceu nenhuma troca
            # isso significa que o array ja esta ordenado
            return
        
array = [42, 15, 16, 1, 0, 100, 88]

print(f"Array fora de ordem: ", array)
bubblesort(array)
print(f"Array em ordem: ", array)
