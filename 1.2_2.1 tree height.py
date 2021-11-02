"""
Sample Input:
10
9 7 5 5 2 9 9 9 2 -1
Sample Output:
4

Sample Input:
5
4 -1 4 1 1
Sample Output:
3

Sample Input:
5
-1 0 4 0 3
Sample Output:
4
"""



def tree_height(parent: list):
    """
    Вычисляет высоту дерева.
    На вход приходит последовательность родителей для каждой вершины

    >>> tree_height([9, 7, 5, 5, 2, 9, 9, 9, 2, -1])
    4

    >>> tree_height([4, -1, 4, 1, 1])
    3

    >>> tree_height([-1, 0, 4, 0, 3])
    4
    """
    # stack_tree = []
    pass

def main():
    number = input()
    parent = [int(i) for i in input().split()]
    print(tree_height(parent))



if __name__ == '__main__':
    import doctest
    doctest.testmod()#verbose=True
    # main()