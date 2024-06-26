"""
Unittest function 'Node' and 'PriorityQueue'
"""

from unittest import TestCase, main
from src.heap_based_priority_queue import Node, PriorityQueue


class FindBiggestElementTest(TestCase):
    def test_insert_element(self):
        pq = PriorityQueue()

        test = Node("test", 100)
        pq.insert_element(test)
        self.assertEqual(len(pq.heap), 1)

    def test_delete_element(self):
        pq = PriorityQueue()

        should_delete = Node("test", 100)
        pq.insert_element(should_delete)
        test1 = Node("test1", 10)
        pq.insert_element(test1)
        test2 = Node("test2", 20)
        pq.insert_element(test2)
        test3 = Node("test2", 30)
        pq.insert_element(test3)
        pq.delete_element(should_delete)
        self.assertEqual(len(pq.heap), 3)

    def test_correct_priority_queue(self):
        pq = PriorityQueue()

        danik = Node("Danik", 300)
        pq.insert_element(danik)

        andrew = Node("Andrew", 20)
        pq.insert_element(andrew)

        vasya = Node("Vasya", 400)
        pq.insert_element(vasya)

        result = [node.priority for node in pq.heap]
        self.assertEqual(result, [400, 20, 300])

    def test_pop_element(self):
        pq = PriorityQueue()

        test = Node("test1", 10)
        pq.insert_element(test)

        pq.pop_element()
        self.assertEqual(len(pq.heap), 0)


if __name__ == '__main__':
    main()
