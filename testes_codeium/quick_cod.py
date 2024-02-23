import unittest
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)
class TestQuicksort(unittest.TestCase):
    def test_lista_vazia(self):
        self.assertEqual(quicksort([]), [])

    def test_lista_com_1_elemento(self):
        self.assertEqual(quicksort([1]), [1])

    def test_lista_com_2_elementos(self):
        self.assertEqual(quicksort([1, 2]), [1, 2])
        self.assertEqual(quicksort([2, 1]), [1, 2])

    def test_lista_com_multiplos_elementos(self):
        self.assertEqual(quicksort([3, 2, 1, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([3, 2, 5, 4, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([5, 2, 4, 1, 3]), [1, 2, 3, 4, 5])
        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()

