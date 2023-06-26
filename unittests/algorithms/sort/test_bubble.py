import random
from .sorting_tests import SortingTests
from algorithms.sort import bubble_sort


class TestBubble(SortingTests):

    def test_regular(self):
        random_values = [random.randint(1, 100) for _ in range(10)]
        self.verify_sorted(bubble_sort, random_values)

    def test_small_list(self):
        random_values = [random.randint(1, 100) for _ in range(2)]
        self.verify_sorted(bubble_sort, random_values)

    def test_empty(self):
        random_values = []
        self.verify_sorted(bubble_sort, random_values)
