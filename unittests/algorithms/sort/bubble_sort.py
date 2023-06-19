import random
from unittests.algorithms.sort.sorting_tests import SortingTests
from algorithms.sort import bubble_sort


class TestBubble(SortingTests):



    def test_regular(self, bubble_sort):
        random_values = [random.randint(1, 100) for _ in range(10)]
        py_sorted = sorted(random_values)
        bb_sorted = bubble_sort(random_values)
        self.assertEqual(py_sorted, bb_sorted)

    def test_small_list(self):
        random_values = [random.randint(1, 100) for _ in range(2)]
        py_sorted = sorted(random_values)
        bb_sorted = bubble_sort(random_values)
        self.assertEqual(py_sorted, bb_sorted)

    def test_empty(self):
        empty_list = []
        py_sorted = sorted(empty_list)
        bb_sorted = bubble_sort(empty_list)
        self.assertEqual(py_sorted, bb_sorted)


