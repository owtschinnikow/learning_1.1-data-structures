import sys

stack_max = []

def push(x):
    """
    Добавляет элемент x в конец стека.
    """
    stack_max.append(x)

def pop():
    """
    Удаляет элемент из конца стека.
    """
    x = stack_max.pop()


def max_stak():
    """
    Выводит последний элемент из конца стека, который максимальный.
    """
    x = stack_max[-1]
    return print(x)


def max_stak_return(n, commamds):
    for i in range(n):
        # print(i, stack_max, commamds[i][0])
        # print(commamds[i+1][0])

        if commamds[i][0] == 'push':
            if len(stack_max) == 0:
                push(int(commamds[i][1]))
            elif stack_max[-1] < int(commamds[i][1]):
                push(int(commamds[i][1]))
            elif stack_max[-1] >= int(commamds[i][1]):
                push(stack_max[-1])

        elif commamds[i][0] == 'max':
            max_stak()

        elif commamds[i][0] == 'pop':
            pop()
    return


def main():
    reader = (line.split() for line in sys.stdin)
    n = int((next(reader))[0])
    commamds = list(reader)
    # print(n)
    # print(commamds)
    max_stak_return(n, commamds)

def test():
    n = 5
    commamds = [['push', '2'], ['push', '1'], ['max'], ['pop'], ['max']]
    max_stak_return(n, commamds)




if __name__ == '__main__':
    # import doctest
    # doctest.testmod()#verbose = True
    main()
    # test()

