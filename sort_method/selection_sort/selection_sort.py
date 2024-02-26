import time


def selection_sort(arr):
    n = len(arr)
    for idx in range(0, n - 1):
        min_idx = idx
        for el in range(idx + 1, n):
            # індекс + 1 тому що ми точно знаємо що минулий елемент є менший за наступний
            if arr[el] < arr[min_idx]:
                time.sleep(0.6)  # затримка для наглядності
                min_idx = el

        arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
        print("\r", array, end="", flush=True)  # результат


array = [10, 2, 3, 1, 4, 6, 5, 8]
selection_sort(array)
