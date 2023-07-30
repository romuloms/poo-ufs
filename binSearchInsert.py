from binary_search import pesquisaBinaria


def binSearch2(list, item):
    value = pesquisaBinaria(list, item)
    if list[value] != item:
        list.insert(value, item)
    return value

example = [0, 2, 5, 7]

# print(binSearch2(example, 2))
binSearch2(example, 6)
print(example)
