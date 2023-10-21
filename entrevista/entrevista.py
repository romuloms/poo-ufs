# array slicing em python
arr = [1,2,3,4,5]
#print(arr[1:3])     ## [2, 3]

# unpacking: designar valores individuais do array às variáveis
a, b, c = [1, 2, 3]
#print(b)

# loops em arrays
# usando index:
#for i in range(len(arr)):
#    print(arr[i])
# sem index:
#for i in arr:
#    print(i)
# com index e valor:
#for i, n in enumerate(arr):
#    print(i, n)    # essa é boa
#--------------------------------

# iterar dois arrays ao mesmo tempo:
arr2 = [6, 7, 8]
#for n1, n2 in zip(arr, arr2):
    # print(n1, n2)

# list comprehension:
# arr3 = [i+i for i in range(5)]
# print(arr3)

# matrizes:
matriz = [[0]*4 for i in range(4)]
# print(matriz)
# matriz[1][0] = 2
# print(matriz)

# combinar lista de strings:
strs = ["ab", "cd", "ef"]
# print("2".join(strs))

# queues:
