"""
Sample Input:
2 5
1 2 3 4 5

Sample Output:
0 0
1 0
0 1
1 2
0 4
"""

from collections import deque
import sys
from queue import PriorityQueue

def parallel_process(cpu_number:int, number:int, packets:list) -> list:
    """
    Функция, которая показывает номер процессора и время начала обработки процесса этим процессором
    :param cpu_number:
    :param number:
    :param packets:
    :return:

    >>> parallel_process(2, 5, [1, 2, 3, 4, 5])
    0 0
    1 0
    0 1
    1 2
    0 4
    >>> parallel_process(2, 15, [0, 0, 1, 0, 0, 0, 2, 1, 2, 3, 0, 0, 0, 2, 1])
    0 0
    0 0
    0 0
    1 0
    1 0
    1 0
    1 0
    0 1
    0 2
    1 2
    0 4
    0 4
    0 4
    0 4
    1 5
    """
    heap = PriorityQueue()
    for i in range(cpu_number):
        heap.put([0,i])

    for i in packets:
        next_item = heap.get()
        print(next_item[1], next_item[0])
        heap.put([next_item[0]+i, next_item[1]])

    return

def main():
    reader = (line.split() for line in sys.stdin)
    cpu_number, number = [int(i) for i in (next(reader))]
    packets = [int(i) for i in (next(reader))]
    # print(cpu_number, number, packets)
    parallel_process(cpu_number, number, packets)


if __name__ == '__main__':
    import doctest
    doctest.testmod()#verbose=True
    main()