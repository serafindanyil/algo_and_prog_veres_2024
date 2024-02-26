import time


def insertion_sort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
        while j >= 0 and key < arr[j]:
            time.sleep(0.6)
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
        print("\r", array, end="", flush=True)  # результат


array = [10, 2, 3, 1, 4, 6, 5, 8]
insertion_sort(array)
