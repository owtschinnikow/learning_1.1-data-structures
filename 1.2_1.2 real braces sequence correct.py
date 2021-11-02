"""
Sample Input 1:
([](){([])})
Sample Output 1:
Success

Sample Input 2:
()[]}
Sample Output 2:
5

Sample Input 3:
{{[()]]
Sample Output 3:
7

Sample Input 4:
foo(bar);
Sample Output 4:
Success

Sample Input 5:
foo(bar[i);
Sample Output 5:
10
"""



def is_braces_sequence_correct(s: str):
    """
    Проверяет корректность скобочной последовательности
    из () [] {} и посторонних символов

    >>> is_braces_sequence_correct("[]")
    'Success'
    >>> is_braces_sequence_correct("{}[]")
    'Success'
    >>> is_braces_sequence_correct("[()]")
    'Success'
    >>> is_braces_sequence_correct("([](){([])})")
    'Success'
    >>> is_braces_sequence_correct("()[]}")
    5
    >>> is_braces_sequence_correct("{{[()]]")
    7
    >>> is_braces_sequence_correct("foo(bar);")
    'Success'
    >>> is_braces_sequence_correct("foo(bar[i);")
    10
    >>> is_braces_sequence_correct("{")
    1
    >>> is_braces_sequence_correct("{[}")
    3
    >>> is_braces_sequence_correct("([](){([])})")
    'Success'
    >>> is_braces_sequence_correct("}()")
    1
    >>> is_braces_sequence_correct("([]")
    1
    >>> is_braces_sequence_correct("[](()")
    3
    >>> is_braces_sequence_correct("abcd{")
    5
    >>> is_braces_sequence_correct("{}([]")
    3
    >>> is_braces_sequence_correct("{}aa(aa[]")
    5
    """


    stack_braces = []                   #стек для хранения скобок, открывающих
    stack_number_braces_open = []       #стек для хранения порядкового номера скобок, открывающих
    stack_number_braces_close = []      #стек для хранения порядкового номера скобок, закрывающих

    for number in range(len(s)):        #просмотр всех символов из строки
        if s[number] not in '()[]{}':   #если номер не любая скобка, то продолжить
            continue
        if s[number] in '([{':                      #если скобка открывающая
            stack_braces.append(s[number])          #, то добавить её в стек скобок
            stack_number_braces_open.append(number+1) #и добавить её порядковый номер в стек номеров открыыающих скобок.
        else:                                       #иначе -
            stack_number_braces_close.append(number+1)  #добавить в стек закрывающих скобок закрывающую скобку.
            if len(stack_braces) == 0:                  #сли пришла закрывающая скобка, а стек пустой
                return stack_number_braces_close.pop()  #, то вызвать номер скобки закрывающей для которой не нашлась пара.

            left = stack_braces.pop()   #иначе - выделение скобки из стека

            if left == '(':             #составление подходящих соотношений скобок
                right = ')'
            elif left == '[':
                right = ']'
            elif left == '{':
                right = '}'

            if right != s[number]:      #если соотношение не верно
                return stack_number_braces_close.pop()  #, то вызвать номер скобки закрывающей для которой пара не правильная
            stack_number_braces_open.pop()
            stack_number_braces_close.pop()

    if len(stack_braces) == 0:          #если все символы кончились и стек пустой, то -
        return 'Success'                #вывести 'Success'
    elif len(stack_number_braces_close) != 0:
        # print('Первый выход')
        return stack_number_braces_close.pop()
    elif len(stack_number_braces_open) != 0:
        # print('Второй выход')
        return stack_number_braces_open.pop()


def main():
    s = input()
    print(is_braces_sequence_correct(s))


if __name__ == '__main__':
    import doctest
    doctest.testmod()#verbose=True
    main()