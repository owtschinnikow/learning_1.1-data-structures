"""
Sample Input 1:
6
0 1 2 3 4 5

Sample Output 1:
0

Sample Input 2:
6
7 6 5 4 3 2

Sample Output 2:
4
2 5
1 4
0 2
2 5

0 <= m <= 4n
"""

import sys


def sort_to_min_heap(n, a_list):
    """
    Функция сообщает количество перестановок необходимых для создания мин функции и сами перестановки
    :return:
    >>> sort_to_min_heap(5, [5, 4, 3, 2, 1])
    3
    1 4
    0 1
    1 3
    >>> sort_to_min_heap(5, [1, 2, 3, 4, 5])
    0
    >>> sort_to_min_heap(6, [7, 6, 5, 4, 3, 2])
    4
    2 5
    1 4
    0 2
    2 5
    """
    pass


def sift_down(i: int, a_list : list):
    """
    Функция просеевания кучи вниз
    Используется если значение измененного элемента увеличивается
    :param i:
    :param a_list:
    :return:

    >>> sift_down(1, [3, 6, 4, 9, 8, 12, 7, 11, 9])
    [3, 6, 4, 9, 8, 12, 7, 11, 9]
    >>> sift_down(1, [3, 10, 4, 9, 8, 12, 7, 11, 9])
    [3, 8, 4, 9, 10, 12, 7, 11, 9]
    """
    while 2 * i + 1 < len(a_list):
        left = 2 * i + 1  # left — левый сын индекс
        right = 2 * i + 2  # right — правый сын индекс
        j = left
        if right < len(a_list) and a_list[right] < a_list[left]:
            j = right
        if a_list[i] <= a_list[j]:
            break
        a_list[i], a_list[j] = a_list[j], a_list[i]
        i = j
    return a_list


def sift_up(i:int, a_list:list):
    """
    Функция просеевания кучи вверх
    Используется если значение измененного элемента уменьшается
    :param i:
    :param a_list:
    :return:
    >>> sift_up(1, [3, 6, 4, 9, 8, 12, 7, 11, 9])
    [3, 6, 4, 9, 8, 12, 7, 11, 9]
    >>> sift_up(1, [3, 5, 4, 9, 8, 12, 7, 11, 9])
    [3, 5, 4, 9, 8, 12, 7, 11, 9]
    >>> sift_up(1, [3, 2, 4, 9, 8, 12, 7, 11, 9])
    [2, 3, 4, 9, 8, 12, 7, 11, 9]
    >>> sift_up(8, [3, 6, 4, 9, 8, 12, 7, 11, 2])
    [2, 3, 4, 6, 8, 12, 7, 11, 9]
    """
    while a_list[i] < a_list[int((i - 1) / 2)]:  # i=0 — корень
        a_list[i], a_list[int((i - 1) / 2)] = a_list[int((i - 1) / 2)], a_list[i]
        i = int((i - 1) / 2)
    return a_list


def main():
    """
    Функция по чтениию данных с системы
    :return:
    """
    reader = (line.split() for line in sys.stdin)
    n = int((next(reader))[0])
    a_list = [int(i) for i in (next(reader))]
    print(n, a_list)
    sort_to_min_heap(n, a_list)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    # main()
    # test()
