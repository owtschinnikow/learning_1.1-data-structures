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
https://neerc.ifmo.ru/wiki/index.php?title=%D0%94%D0%B2%D0%BE%D0%B8%D1%87%D0%BD%D0%B0%D1%8F_%D0%BA%D1%83%D1%87%D0%B0#.D0.A1.D0.BC._.D1.82.D0.B0.D0.BA.D0.B6.D0.B5
"""

import sys

m = 0
sort_list = []

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
    global m
    global sort_list
    while 2 * i + 1 < len(a_list):
        left = 2 * i + 1  # left — левый сын индекс
        right = 2 * i + 2  # right — правый сын индекс
        j = left
        if right < len(a_list) and a_list[right] < a_list[left]:
            j = right
        if a_list[i] <= a_list[j]:
            break
        # print('i, j', i, j)
        sort_list.append([i, j])
        a_list[i], a_list[j] = a_list[j], a_list[i]
        i = j
        m += 1
    # print('m', m)
    # print('sort_list', sort_list)
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


def extract_min(a_list:list):
    """
    Функция выполняет извлечение минимального элемента из кучи
    :param a_list:
    :return:
    >>> extract_min([1, 2, 3, 4, 5])
    (1, [2, 4, 3, 5])
    """
    min = a_list[0]
    a_list[0] = a_list.pop()
    sift_down(0, a_list)
    return min, a_list


def insert(key:int, a_list:list):
    """
    Функция выполняет добавление элемента в кучу.
    :param key:
    :param a_list:
    :return:
    >>> insert(10, [1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5, 10]
    >>> insert(1, [1, 2, 3, 4, 5])
    [1, 2, 1, 4, 5, 3]
    """
    a_list.append(key)
    sift_up(len(a_list) - 1, a_list)
    return a_list


def build_heap_slow(a_list_:list):
    """
    Функция построения кучи с первого элемента из массива.
    :param a_list:
    :return:
    """
    a_list = a_list_.copy()
    b_list = []
    b_list.append(a_list.pop())
    for i in a_list:
        insert(i, b_list)
    return b_list


def build_heap_fast(a_list_:list):
    c_list = a_list_
    for i in range(len(c_list), -1, -1):
        sift_down(i, c_list)
    return c_list


def build_heap_fast_with_index(a_list_:list):
    c_list = a_list_

    for i in range(len(c_list), -1, -1):
        sift_down(i, c_list)
    return c_list

a_list_ = [7, 6, 5, 4, 3, 2]

def main_build_heap_slow(a_list_):
    print(a_list_)
    print(build_heap_slow(a_list_), '\n')


def main_build_heap_fast(a_list_):
    print(a_list_)
    print(*build_heap_fast(a_list_))
    print('m', m)
    print(sort_list)
    for i in sort_list:
        print(*i)


def main():
    """
    Функция по чтениию данных с системы
    :return:
    """
    reader = (line.split() for line in sys.stdin)
    n = int((next(reader))[0])
    a_list = [int(i) for i in (next(reader))]
    build_heap_fast(a_list)
    print(m)
    for i in sort_list:
        print(*i)



if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    # main_build_heap_slow(a_list_)
    # main_build_heap_fast(a_list_)
    main()
