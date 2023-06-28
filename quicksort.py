def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)


arr = [1, 2, 3, 4, 5, 6]
# print(quicksort([10, 2, 1, 3, 15, 20, 0]))
