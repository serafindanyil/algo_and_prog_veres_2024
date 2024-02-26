"""
The main file. Level 2, variant 3
"""

from find_biggest_element import find_biggest_element

if __name__ == '__main__':
    array = [30, 2, 35, 10, 5, 6, 5, 8]
    index, value, k = find_biggest_element(array, 6)
    print(f'Задане k: {k} Знайдений {index + 1}-й найбільший елемент: {value}. '
          f'Позиція {index + 1}-го найбільшого елемента в масиві: {index}.')

