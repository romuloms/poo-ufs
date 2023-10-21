# array slicing em python
arr = [1,2,3,4,5]
print(arr[1:3])     ## [2, 3]

# unpacking: designar valores individuais do array às variáveis
a, b, c = [1, 2, 3]
print(b)

# loops em arrays
# usando index:
for i in range(len(arr)):
   print(arr[i])
# sem index:
for i in arr:
   print(i)
# com index e valor:
for i, n in enumerate(arr):
   print(i, n)    # essa é boa
#--------------------------------

# iterar dois arrays ao mesmo tempo:
arr2 = [6, 7, 8]
for n1, n2 in zip(arr, arr2):
    print(n1, n2)

# list comprehension:
arr3 = [i+i for i in range(5)]
print(arr3)

# matrizes:
matriz = [[0]*4 for i in range(4)]
print(matriz)
matriz[1][0] = 2
print(matriz)

# combinar lista de strings:
strs = ["ab", "cd", "ef"]
print("2".join(strs))

# queues:
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)
queue.popleft()
print(queue)
queue.appendleft(1)
queue.pop()

# hashsets: busca e insercao constantes mas n pode ter duplicados
myset = set()
myset.add(1)
myset.add(2)
print(len(myset))
print(1 in myset)
myset.remove(2)

# lista -> set:
print(set([1,2,3]))

# set comprehension:
mys = {i for i in range(5)}
print(mys)

# hashmap (dicionarios, tbm nao podem ter duplicados):
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 30
print(myMap)
print("alice" in myMap)
myMap.pop("alice")
print(myMap)

# dict comprehension:
myDict = {i: 2*i for i in range(3)}
print(myDict)
# loops em dicionarios:
for key in myMap:
    print(key, myMap[key])
for val in myMap.values():
    print(val)
for key, val in myMap.items():
    print(key, val)

# tuplas (sao imutaveis e podem ser usadas como chaves na busca em dic):
tup = (1,2,3)
newMap = {(1,2): 3}
print(newMap[(1,2)])

# heaps:
import heapq
minH = []
heapq.heappush(1)