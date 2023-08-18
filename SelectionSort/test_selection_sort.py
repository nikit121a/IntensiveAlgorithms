from random import randint

from selection_sort import selection_sort


def test_selection_sort():
    array = []
    for i in range(5):
        array = [randint(0, 100) for j in range(10)]

    assert selection_sort(array) == sorted(array)

    array = [0]
    assert selection_sort(array) == sorted(array)
    array = [-1, -2, 4]
    assert selection_sort(array) == sorted(array)
    array = [-1, -1, -1]
    assert selection_sort(array) == sorted(array)
    array = [2, 2, -5]
    assert selection_sort(array) == sorted(array)


test_selection_sort()
