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


def maximum_in_a_sliding_window(n, a_list, m):
    """
    >>> maximum_in_a_sliding_window(8, [2, 7, 3, 1, 5, 2, 6, 2], 4)
    7 7 5 6 6
    >>> maximum_in_a_sliding_window(3, [2, 1, 5], 1)
    2 1 5
    >>> maximum_in_a_sliding_window(15, [73, 65, 24, 14, 44, 20, 65, 97, 27, 6, 42, 1, 6, 41, 16], 7)
    73 97 97 97 97 97 97 97 42
    >>> maximum_in_a_sliding_window(15, [28, 7, 64, 40, 68, 86, 80, 93, 4, 53, 32, 56, 68, 18, 59], 12)
    93 93 93 93
    >>> maximum_in_a_sliding_window(15, [16, 79, 20, 19, 43, 72, 78, 33, 40, 52, 70, 79, 66, 43, 60], 12)
    79 79 79 79
    >>> maximum_in_a_sliding_window(15, [34, 51, 61, 90, 26, 84, 2, 25, 7, 8, 25, 78, 21, 47, 25], 3)
    61 90 90 90 84 84 25 25 25 78 78 78 47
    >>> maximum_in_a_sliding_window(15, [27, 83, 29, 77, 6, 3, 48, 2, 16, 72, 46, 38, 55, 2, 58], 5)
    83 83 77 77 48 72 72 72 72 72 58
    """

    stack_max_in = []
    stack_max_out = []
    stack_res = []

    if m == 1:
        return print(*a_list) #, 'stack_max_in', stack_max_in, 'stack_max_out', stack_max_out)

    for i in range(m-1, -1, -1):
        if len(stack_max_out) == 0:
            stack_max_out.append([a_list[i], a_list[i]])
        elif stack_max_out[-1][1] < a_list[i]:
            stack_max_out.append([a_list[i], a_list[i]])
        elif stack_max_out[-1][1] >= a_list[i]:
            stack_max_out.append([a_list[i], stack_max_out[-1][1]])

    print('chek_1', 'stack_max_in =', stack_max_in, 'stack_max_out =', stack_max_out, 'stack_res =', stack_res)

    for i in range(m, len(a_list)):
    # while len(stack_max_in) + len(stack_max_out) == m:
        print('chek_2', 'i =', i, 'a_list[i] =', a_list[i])
        print('chek_2.1', 'stack_max_in =', stack_max_in, 'stack_max_out =', stack_max_out, 'stack_res =', stack_res)



        # if (len(stack_max_in) <= m) and (len(stack_max_out) <= m) and (len(stack_max_in)+len(stack_max_out) == m):
        # # for i in range(m, len(a_list)):
        #     print('chek_3', 'stack_max_in =', stack_max_in, 'stack_max_out =', stack_max_out, 'stack_res =', stack_res)

        if len(stack_max_in) == 0:
            print('chek_4', 'stack_max_in =', stack_max_in, 'stack_max_out =', stack_max_out, 'stack_res =', stack_res)
            stack_res.append(stack_max_out[-1][1]) #print(stack_max_out[-1][1])
            stack_max_out.pop()
            stack_max_in.append([a_list[i], a_list[i]])
            print('chek_4.1', 'stack_max_in =', stack_max_in, 'stack_max_out =', stack_max_out, 'stack_res =', stack_res)


        else:
            while len(stack_max_in) + len(stack_max_out) == m:

                if len(stack_max_out)  == 0:
                    break

                elif stack_max_out[-1][1] >= stack_max_in[-1][1]:
                    print('chek_6', 'stack_max_in =', stack_max_in, 'stack_max_out =', stack_max_out, 'stack_res =', stack_res)
                    stack_res.append(stack_max_out[-1][1]) #print(stack_max_out[-1][1])
                    stack_max_out.pop()
                    if stack_max_in[-1][1] < a_list[i]:
                        stack_max_in.append([a_list[i], a_list[i]])
                    elif stack_max_in[-1][1] >= a_list[i]:
                        stack_max_in.append([a_list[i], stack_max_in[-1][1]])
                    print('chek_6.1', 'stack_max_in =', stack_max_in, 'stack_max_out =', stack_max_out, 'stack_res =', stack_res)

                elif stack_max_out[-1][1] < stack_max_in[-1][1]:
                    print('chek_7', 'stack_max_in =', stack_max_in, 'stack_max_out =', stack_max_out, 'stack_res =', stack_res)
                    stack_res.append(stack_max_in[-1][1]) #print(stack_max_in[-1][1])
                    stack_max_out.pop()
                    if stack_max_in[-1][1] < a_list[i]:
                        stack_max_in.append([a_list[i], a_list[i]])
                    elif stack_max_in[-1][1] >= a_list[i]:
                        stack_max_in.append([a_list[i], stack_max_in[-1][1]])
                    print('chek_7.1', 'stack_max_in =', stack_max_in, 'stack_max_out =', stack_max_out, 'stack_res =', stack_res)


        if len(stack_max_out) == 0:
            print('chek_5', 'stack_max_in =', stack_max_in, 'stack_max_out =', stack_max_out, 'stack_res =', stack_res)
            stack_max_out, stack_max_in = stack_max_in[::-1], []
            print('chek_5.1', 'stack_max_in =', stack_max_in, 'stack_max_out =', stack_max_out, 'stack_res =', stack_res)




    return print('chek_OUT', 'stack_max_in =', stack_max_in, 'stack_max_out =', stack_max_out, 'stack_res =', stack_res)


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

