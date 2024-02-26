import time


def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for idx in range(n - 1):
        for el in range(0, n-idx-1):
            time.sleep(0.4)
            if arr[el] > arr[el + 1]:
                swapped = True
                arr[el], arr[el + 1] = arr[el + 1], arr[el]
            if not swapped:
                return
        print("\r", arr, end="", flush=True)


bubble_sort([10, 2, 3, 1, 4, 6, 5, 8, 9, 7])
