"""Heap queue (or heapq) in Python
https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
https://docs.python.org/3/library/heapq.html
"""

import heapq
from queue import PriorityQueue
from math import inf, isinf

def heap_basics():
    # initializing list
    li = [5, 7, 9, 1, 3]

    # Transform list x into a heap, in-place, in linear time.
    heapq.heapify(li)
    print(li)           # the order is not smallest to biggest, instead, it represents a heap
    print(type(li))     # li is a heap, although its type is list.
    print()

    # using heappush() to push elements into heap
    # pushes 4
    heapq.heappush(li,4)
    print(li)
    print(type(li))
    print()

    # pop
    print("pop the heap now:")
    while li:
        print(heapq.heappop(li))
# heap_basics()

def tuple_heap_elements():
    h = []
    heapq.heappush(h, (5, 'write code'))
    heapq.heappush(h, (7, 'release product'))
    heapq.heappush(h, (1, 'write spec'))
    heapq.heappush(h, (3, 'create tests'))
    print(h)
    # 1
    # r1 = heapq.heappop(h)
    # r2 = heapq.heappop(h)
    # print(r1, r2)

    # 2
    # print(h[0][0])
# tuple_heap_elements()

def update_the_priority_of_a_heap():
    """heapq library doesn't support this operation, there are serval ways to solve this problem.
    https://stackoverflow.com/questions/46636656/python-heapq-replace-priority
        https://pypi.org/project/priorityq/
        https://github.com/ActiveState/code/blob/master/recipes/Python/577892_Dijkstrshortest_path/recipe-577892.py
    https://docs.python.org/3/library/heapq.html#module-heapq
    """

    # update the heap by using _siftdown and _siftup    -- O(n) running time
    # print(hasattr(heapq, "_siftdown"))
    # print(hasattr(heapq, "_siftup"))

    # construct a priority heap
    h = []
    heapq.heapify(h)

    node_1 = (5, 'node 1')
    node_2 = (7, 'node 2')
    node_3 = (1, 'node 3')
    node_4 = (3, 'node 4')
    node_5 = (10, 'node 5')
    
    heapq.heappush(h, node_1)
    heapq.heappush(h, node_2)
    heapq.heappush(h, node_3)
    heapq.heappush(h, node_4)
    heapq.heappush(h, node_5)

    # _siftdown
    # update priority of node 5
    idx = h.index(node_5)
    print(h[idx] == node_5)
    h[idx] = (6, 'node 5')
    # update the heap
    heapq._siftdown(h, 0, idx)

    # check if successed
    print([heapq.heappop(h) for i in range(len(h))])

# update_the_priority_of_a_heap()


def infinite_key_test():
    h = []
    heapq.heapify(h)

    node_1 = (inf, 'node 1')
    node_2 = (inf, 'node 2')
    node_3 = (1, 'node 3')
    node_4 = (3, 'node 4')
    heapq.heappush(h, node_1)
    heapq.heappush(h, node_2)
    heapq.heappush(h, node_3)
    heapq.heappush(h, node_4)

    # 1
    print([heapq.heappop(h) for i in range(len(h))])

    # 2
    # while h:
    #     if not isinf(h[0][0]):
    #         print(heapq.heappop(h))
    #     else:
    #         break
# infinite_key_test()

def change_key_test():
    h = []
    heapq.heapify(h)

    node_1 = (inf, 'node 1')
    node_2 = (inf, 'node 2')
    node_3 = (1, 'node 3')
    node_4 = (3, 'node 4')
    heapq.heappush(h, node_1)
    heapq.heappush(h, node_2)
    heapq.heappush(h, node_3)
    heapq.heappush(h, node_4)

    print(h)
    node_1 = (4, 'node 1 changed')
    print(h)

    h[h.index(node_2)] = (4, 'node 2 changed')
    print(h)
# change_key_test()

def entry_finder_test():
    h = []
    heapq.heapify(h)

    node_1 = (inf, 'node 1')
    node_2 = (inf, 'node 2')
    node_3 = (1, 'node 3')
    node_4 = (3, 'node 4')
    heapq.heappush(h, node_1)
    heapq.heappush(h, node_2)
    heapq.heappush(h, node_3)
    heapq.heappush(h, node_4)

    print(h[0] == node_3)
    print(h[0] == (1, 'node 3'))
# entry_finder_test()

def heapify_list_of_tuples():
    # look at this: https://stackoverflow.com/questions/43477958/typeerror-not-supported-between-instances-python
    node_1 = (inf, 'node 1')
    node_2 = (inf, 'node 2')
    node_3 = (1, 'node 3')
    node_4 = (3, 'node 4')
    h = [node_1, node_2, node_3, node_4]
    heapq.heapify(h)
    print(h)
# heapify_list_of_tuples()
