def mergeSort(arr):
    if len(arr) > 1:
        # Divide o array ao meio
        meio = len(arr) // 2
        # OBS: [:] é similar ao spread operator ... 
        metadeEsquerda = arr[:meio]
        metadeDireita = arr[meio:]
        # Recursivamente, ordena as duas metades
        mergeSort(metadeEsquerda)
        mergeSort(metadeDireita)
        # Inicializa os indices para percorrer as duas metades e o indice para o array final
        i = j = k = 0
        # Copia os dados para arrays temporarios metadeEsquerda e metadeDireita
        while i < len(metadeEsquerda) and j < len(metadeDireita):
            if metadeEsquerda[i] < metadeDireita[j]:
                arr[k] = metadeEsquerda[i]
                i += 1
            else:
                arr[k] = metadeDireita[j]
                j += 1
            k += 1
        # Verifica se ha elementos restantes nas duas metades e os copia, se houver
        while i < len(metadeEsquerda):
            arr[k] = metadeEsquerda[i]
            i += 1
            k += 1
        while j < len(metadeDireita):
            arr[k] = metadeDireita[j]
            j += 1
            k += 1

# Exemplo de uso:
arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr)
print("Array ordenado:", arr)
