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
    def __init__(self, value, priority=0):
        self.value = value
        self.priority = priority


class PriorityQueue:
    HEAP = [] # Відсортована бінарна хіпа

    def up(self, i):
        while i != 0 and self.HEAP[i].priority > self.HEAP[(i - 1) // 2].priority:
            self.HEAP[i], self.HEAP[(i - 1) // 2] = self.HEAP[(i - 1) // 2], self.HEAP[i]
            i = (i - 1) // 2

    def down(self, i):
        n = len(self.HEAP)
        while 2 * i + 1 < n:
            max_child = 2 * i + 1
            if max_child + 1 < n and self.HEAP[max_child].priority < self.HEAP[max_child + 1].priority:
                max_child += 1
            if self.HEAP[i].priority >= self.HEAP[max_child].priority:
                break
            self.HEAP[i], self.HEAP[max_child] = self.HEAP[max_child], self.HEAP[i]
            i = max_child

    def insert_element(self, obj):
        self.HEAP.append(obj)
        self.up(len(self.HEAP) - 1)

    def delete_element(self, obj):
        obj_index = None
        n = len(self.HEAP)
        for index in range(0,n):
            if obj == self.HEAP[index]:
                obj_index = index
        self.HEAP[obj_index], self.HEAP[n-1] = self.HEAP[n-1], self.HEAP[obj_index]
        self.HEAP.pop(n-1)
        self.down(obj_index)

    def show_priority_queue_with_change(self):
        for node in self.HEAP:
            print(f"Value: {node.value}, Priority: {node.priority}")


pq = PriorityQueue()

danik = Node("Danik", 300)
pq.insert_element(danik)

andrew = Node("Andrew", 20)
pq.insert_element(andrew)

kolya = Node("Kolya", 22)
pq.insert_element(kolya)

sergey = Node("Sergey", 31)
pq.insert_element(sergey)

igor = Node("Igor", 21)
pq.insert_element(igor)

nazar = Node("Nazar", 322)
pq.insert_element(nazar)

vasya = Node("Vasya", 400)
pq.insert_element(vasya)

pq.delete_element(vasya)
pq.show_priority_queue_with_change()



