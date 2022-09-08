""" 
https://docs.python.org/2/library/collections.html#deque-objects
Deques are a generalization of stacks and queues (the name is pronounced “deck” and 
is short for “double-ended queue”). Deques support thread-safe, memory efficient appends 
and pops from either side of the deque with approximately the same O(1) performance 
in either direction.
"""

from collections import deque

def basic_operations():
    dq = deque()
    dq.append(5)
    dq.append(6)
    dq.appendleft(2)
    print(dq)

    right = dq.pop()
    left = dq.popleft()
    print(left, right, dq)

    dq[0] = 10
    print(dq)
# basic_operations()

def find_elements_in_deque():
    dq = deque()
    dq.append(5)
    dq.append(6)
    dq.appendleft(2)
    print(5 in dq)
    print(dq[0])
# find_elements_in_deque()

def errors():
    dq = deque()
    # print(dq[0])      # IndexError
    print(5 not in dq)
errors()

# see more examples here: https://docs.python.org/2/library/collections.html#deque-objects
