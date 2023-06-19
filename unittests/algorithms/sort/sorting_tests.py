import pytest
import random


class SortingTests:

    def test_regular(self, sorting_func):
        random_values = [random.randint(1, 100) for _ in range(10)]
        py_sorted = sorted(random_values)
        bb_sorted = sorting_func(random_values)
        self.assertEqual(py_sorted, bb_sorted)

    def test_small_list(self, sorting_func):
        random_values = [random.randint(1, 100) for _ in range(2)]
        py_sorted = sorted(random_values)
        bb_sorted = sorting_func(random_values)
        self.assertEqual(py_sorted, bb_sorted)

    def test_empty(self, sorting_func):
        empty_list = []
        py_sorted = sorted(empty_list)
        bb_sorted = sorting_func(empty_list)
        self.assertEqual(py_sorted, bb_sorted)