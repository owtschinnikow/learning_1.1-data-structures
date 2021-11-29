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


def сoncatenating_tables():
    pass


def make_set(i):
    parent = []
    parent[i] = i
    return parent


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
    reader = (line.split() for line in sys.stdin)
    data_number, call_number = [int(i) for i in (next(reader))]  # Количество таблиц, количество вызово таблиц
    data_original = [int(i) for i in (next(reader))]  # Начальное количество строк в таблицах
    call_commands_list = [list(map(int, next(reader))) for i in range(call_number)]  # команды вызовов таблиц для слияния (в / из)
    # print(data_number, call_number, data_original)
    # print((call_commands_list))
    # сoncatenating_tables(cpu_number, number, packets)


if __name__ == '__main__':
    import doctest
    doctest.testmod()#verbose=True
    main()