from typing import List


def selection_sort(array: List[int]) -> List[int]:
    """
    Sorts the array in ascending order using selection sort

    Args:
        array (List[int]): input

    Returns:
        List[int]: sorted array
    """
    sort = 0
    for i in range(len(array)):
        for j in range(sort, len(array)):
            if array[j] == min(array[sort:len(array)]):
                array[j], array[sort] = array[sort], array[j]
        sort += 1
    return array


# https://leetcode.com/problems/sort-colors/
