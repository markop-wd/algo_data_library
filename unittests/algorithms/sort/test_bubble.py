import random
from unittests.algorithms.sort.sorting_tests import SortingTests
from algorithms.sort import bubble_sort


class TestBubble(SortingTests):

    def test_regular(self):
        super().test_regular(bubble_sort)

    def test_small_list(self):
        super().test_small_list(bubble_sort)

    def test_empty(self):
        super().test_empty(bubble_sort)
