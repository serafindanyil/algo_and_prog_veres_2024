"""
Function 'find_biggest_element'
"""


def find_biggest_element(array, k: int):
    """
    selection_sort
    """

    max_index = 0
    n = len(array)

    if not array:
        raise ValueError(f'Array is empty')

    if n < k:
        raise ValueError(f'Array size is small than k. Len array: {n} < k: {k}')

    if not all(isinstance(x, int) for x in array):
        raise TypeError(f'Data type is invalid. The function accepts type: int')

    for index in range(0, k):
        for el in range(index + 1, k):
            if array[el] > array[max_index]:
                max_index = el

    return max_index, array[max_index], k
