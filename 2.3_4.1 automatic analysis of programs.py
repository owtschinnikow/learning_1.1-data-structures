"""
Sample Input 1:
4 6 0
1 2
1 3
1 4
2 3
2 4
3 4

Sample Output 1:
1

Sample Input 2:
4 6 1
1 2
1 3
1 4
2 3
2 4
3 4
1 2

Sample Output 2:
0

Sample Input 3:
4 0 6
1 2
1 3
1 4
2 3
2 4
3 4

Sample Output 3:
1
"""

import sys

def analysic_equal(number_of_variables, number_of_calls_equal, number_of_calls_not_equal, call_commands_list):
    """
    Функция анализирует выполнима ли система равенств и неравенств
    :param number_of_variables:
    :param number_of_calls_equal:
    :param number_of_calls_not_equal:
    :param call_commands_list:
    :return:
    """
    parent, rank = make_set(number_of_variables)
    for number, comand in enumerate(call_commands_list):
        if number <= number_of_calls_equal-1:
            union_tree(comand[1], comand[0], parent, rank)
        else:
            if find_i(comand[1], parent) == find_i(comand[0], parent):
                return print(0)
    return print(1)

def union_tree(i:int, j:int, parent:list, rank:list):
    """
    Функция пробует объединять деревья, которые относятся к i и j.
    Если это уже одно дерево, то ничего не происходит
    Если поменялся rank, то он пересчитывается.
    :param i:
    :param j:
    :param parent:
    :param rank:
    :return:
    """
    global max_data
    i_id, j_id = find_i(i, parent), find_i(j, parent)
    if i_id == j_id:
        return
    if rank[i_id-1] > rank[j_id-1]:
        parent[j_id-1] = i_id
    else:
        parent[i_id-1] = j_id
        if rank[i_id-1] == rank[j_id-1]:
            rank[j_id-1] += 1


def make_set(data_number):
    """
    Функция делает
    базовый массив деревьев и
    массив rank
    для хранения высоты поддерева по его заданной длине data_number.
    :param data_number:
    :return:
    """
    parent = []
    rank = []
    for i in range(1, data_number+1):
        parent.append(i)
        rank.append(0)
    return parent, rank


def find_i(i:int, parent:list) -> int:
    """
    Функция которая находит корень дерева для элемента i
    :param i:
    :param parent:
    :return:
    """
    while i != parent[i-1]:
        i = parent[i-1]
    return i


def main():
    """
    Функция обрабатывает ввод в программу, запускает нужные функции
    :return:
    """
    reader = (line.split() for line in sys.stdin)
    number_of_variables, number_of_calls_equal, number_of_calls_not_equal = [int(i) for i in (next(reader))]  # Количество таблиц, количество вызовов таблиц
    call_commands_list = [list(map(int, next(reader))) for i in range(number_of_calls_equal+number_of_calls_not_equal)]  # команды вызовов таблиц для слияния (в / из)
    analysic_equal(number_of_variables, number_of_calls_equal, number_of_calls_not_equal, call_commands_list)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()#verbose=True
    main()
