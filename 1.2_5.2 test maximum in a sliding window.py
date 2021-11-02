"""
Sample Input 1:
3
2 1 5
1
Sample Output 1:
2 1 5

Sample Input 2:
8
2 7 3 1 5 2 6 2
4
Sample Output 2:
7 7 5 6 6
"""

import sys

stack_max_in = []
stack_max_out = []




def maximum_in_a_sliding_window(n, a_list, m):
    """
    >>> maximum_in_a_sliding_window(8, [2, 7, 3, 1, 5, 2, 6, 2], 4)
    7 7 5 6 6
    >>> maximum_in_a_sliding_window(3, [2, 1, 5], 1)
    2 1 5
    """
    print('n', n, 'a_list', a_list, 'm', m)
    print('stack_max_out', stack_max_out, 'stack_max_in', stack_max_in)
    if m == 1:
        stack_max_out.append([1])
        stack_max_in.append([1])
        return print(*a_list), print('stack_max_out', stack_max_out, 'stack_max_in', stack_max_in)



    return print('error_1')


def main():
    reader = (line.split() for line in sys.stdin)
    n = int((next(reader))[0])
    a_list = [int(i) for i in (next(reader))]
    m = int((next(reader))[0])
    print(n)
    print(a_list)
    print(m)
    maximum_in_a_sliding_window(n, a_list, m)


def test():
    print('test #1')
    n = 8
    a_list = [2, 7, 3, 1, 5, 2, 6, 2]
    m = 1
    assert maximum_in_a_sliding_window(n, a_list, m) == print('2 7 3 1 5 2 6 2'), 'Fail, test #1'

    print('\n' ,'test #2', sep='')
    n = 8
    a_list = [2, 7, 3, 1, 5, 2, 6, 2]
    m = 4
    assert maximum_in_a_sliding_window(n, a_list, m) == print('7 7 5 6 6'), 'Fail, test #2'
    print('\n' ,'test #3', sep='')
    n = 3
    a_list = [2, 1, 5]
    m = 1
    assert maximum_in_a_sliding_window(n, a_list, m) == print('2 1 5'), 'Fail, test #3'
    print('\n' ,'test #4', sep='')
    n = 3
    a_list = [2, 1, 5]
    m = 2
    assert maximum_in_a_sliding_window(n, a_list, m) == print('2 5'), 'Fail, test #4'


if __name__ == '__main__':
    import doctest
    doctest.testmod()#verbose = True
    # main()
    # test()

