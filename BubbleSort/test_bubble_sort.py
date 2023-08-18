from random import randint

from bubble_sort import bubble_sort


def test_bubble_sort():
    array = []
    for i in range(5):
        array = [randint(0, 100) for j in range(10)]
    assert bubble_sort(array) == sorted(array)
    array = [0]
    assert bubble_sort(array) == sorted(array)
    array = [-1, -2, 4]
    assert bubble_sort(array) == sorted(array)
    array = [-1, -1, -1]
    assert bubble_sort(array) == sorted(array)
    array = [2, 2, 2]
    assert bubble_sort(array) == sorted(array)

test_bubble_sort()