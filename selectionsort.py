def selectionSort(arr):
    n = len(arr)
    # Muitas iteracoes
    for i in range(n):
        # Encontra o indice do menor elemento restante no array nao ordenado
        minIndex = i
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # Troca o elemento atual com o menor elemento encontrado
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

arr = [64, 25, 12, 22, 11]
selectionSort(arr)
print("Array ordenado:", arr)
# OBS.: O(log n^2), pessimo
