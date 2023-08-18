from random import randint

from insertion_sort import insertion_sort


def test_insertion_sort():
    array = []
    for i in range(5):
        array = [randint(0, 100) for j in range(10)]

    assert insertion_sort(array) == sorted(array)
    # array = [0]
    # assert insertion_sort(array) == sorted(array)
    # array = [-1, -2, 4]
    # assert insertion_sort(array) == sorted(array)
    # array = [-1, -1, -1]
    # assert insertion_sort(array) == sorted(array)
    # array = [2, 2, 2]
    # assert insertion_sort(array) == sorted(array)



test_insertion_sort