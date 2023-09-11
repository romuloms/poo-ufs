tuplex = (5, 7, 3, 1)
print(tuplex)
tuplex = tuplex + (6,)
print(tuplex)
tuplex = tuplex[:3] + (2, 8, 4) + tuplex[:len(tuplex) - 2]
print(tuplex)