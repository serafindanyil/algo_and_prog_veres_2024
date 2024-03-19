from heap_based_priority_queue import Node, PriorityQueue
"""
The main file. Level 2, variant 1
"""


if __name__ == '__main__':
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

    # pq.delete_element(vasya)

    for node in PriorityQueue.HEAP:
        print(f"Value: {node.value}, Priority: {node.priority}")

