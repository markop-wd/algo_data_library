from typing import List, Callable


class SortingTests:

    @staticmethod
    def verify_sorted(sorting_func: Callable, random_value_list: List[int]):
        py_sorted = sorted(random_value_list)
        my_sorted = sorting_func(random_value_list)
        assert py_sorted == my_sorted
