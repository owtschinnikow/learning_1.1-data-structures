"""
Sample Input:
5 5
1 1 1 1 1
3 5
2 4
1 4
5 4
5 3

Sample Output:
2
2
3
5
5
"""
import sys


max_data = 0



def сoncatenating_tables(data_number:int, call_number:int, data_original:list, call_commands_list:list):
    global max_data
    parent, rank = make_set(data_number)
    # print('parent_0, rank_0 = ', parent, rank)
    for bases in call_commands_list:
        # print('bases', bases)
        union_tree(bases[1], bases[0], parent, rank, data_original)
        # print('parent, rank = ', parent, rank)
        # print('data_original', data_original, 'max_data_original', max(data_original))
        print(max_data)

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


def union_tree(i:int, j:int, parent:list, rank:list, data_original):
    """
    Функция пробует объединять деревья, которые относятся к i и j.
    Если это уже одно дерево, то ничего не происходит
    Если поменялся rank, то он пересчитывается.
    + функция объединяет значение каждого дерева в ячейке назначения, исходную ячейку оно делает - 0
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
        data_original[i_id-1] = data_original[i_id-1] + data_original[j_id-1]
        if max_data < data_original[i_id-1]:
            max_data = data_original[i_id-1]
        data_original[j_id - 1] = 0
        parent[j_id-1] = i_id
    else:
        data_original[j_id - 1] = data_original[i_id - 1] + data_original[j_id - 1]
        if max_data < data_original[j_id - 1]:
            max_data = data_original[j_id - 1]
        data_original[i_id - 1] = 0
        parent[i_id-1] = j_id
        if rank[i_id-1] == rank[j_id-1]:
            rank[j_id-1] += 1


def main():
    """
    Функция обрабатывает ввод в программу, запускает нужные функции
    :return:
    """
    global max_data
    reader = (line.split() for line in sys.stdin)
    data_number, call_number = [int(i) for i in (next(reader))]  # Количество таблиц, количество вызовов таблиц
    data_original = [int(i) for i in (next(reader))]  # Начальное количество строк в таблицах
    call_commands_list = [list(map(int, next(reader))) for i in range(call_number)]  # команды вызовов таблиц для слияния (в / из)
    max_data = max(data_original)
    сoncatenating_tables(data_number, call_number, data_original,call_commands_list)



if __name__ == '__main__':
    # import doctest
    # doctest.testmod()#verbose=True
    main()