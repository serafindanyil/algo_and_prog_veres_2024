"""
Реалізуйте структуру даних "черга з пріоритетами" на основі бінарної купи binary heap, в якому кожен батьківський елемент має вищий пріоритет, ніж пріоритети його дітей.

Якщо у двох елементів однаковий пріоритет, то батьківський елемент може мати пріоритет, ідентичний пріоритету одного або обох його дітей.

Операції, які підтримує ваша черга:

Вставка елемента з заданим значенням та пріоритетом до черги.
Видалення та повернення елемента з найвищим пріоритетом з черги.
Перегляд черги без її зміни.
Для реалізації такої черги з пріоритетами слід використати окремий клас Node, де кожен елемент буде мати два поля: значення та пріоритет.
При вставці елемента до черги, його потрібно розмістити у відповідному порядку з урахуванням пріоритету.
При видаленні елемента з найвищим пріоритетом, на його місце слід розмістити елемент з наступним найвищим пріоритетом.
"""


class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def up(self, i):
        while i != 0 and self.heap[i].priority > self.heap[(i - 1) // 2].priority:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    def down(self, i):
        n = len(self.heap)
        while 2 * i + 1 < n:
            max_child = 2 * i + 1
            if max_child + 1 < n and self.heap[max_child].priority < self.heap[max_child + 1].priority:
                max_child += 1
            if self.heap[i].priority >= self.heap[max_child].priority:
                break
            self.heap[i], self.heap[max_child] = self.heap[max_child], self.heap[i]
            i = max_child

    def insert_element(self, obj):
        self.heap.append(obj)
        self.up(len(self.heap) - 1)

    def delete_element(self, obj):
        obj_index = None
        n = len(self.heap)
        for index in range(0, n):
            if obj == self.heap[index]:
                obj_index = index
        self.heap[obj_index], self.heap[n - 1] = self.heap[n - 1], self.heap[obj_index]
        self.heap.pop(n - 1)
        self.down(obj_index)

    def pop_element(self):
        if not self.heap:
            return None
        obj = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.down(0)
        return obj.value, obj.priority
