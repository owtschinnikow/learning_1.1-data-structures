"""
Sample Input 1:
12
add 911 police
add 76213 Mom
add 17239 Bob
find 76213
find 910
find 911
del 910
del 911
find 911
find 76213
add 76213 daddy
find 76213

Sample Output 1:
Mom
not found
police
not found
Mom
daddy

Sample Input 2:
8
find 3839442
add 123456 me
add 0 granny
find 0
find 123456
del 0
del 0
find 0

Sample Output 2:
not found
granny
me
not found
"""
import sys


phone_book = {}


def main():
    """
    Функция обрабатывает ввод в программу, запускает нужные функции
    :return:
    """
    reader = (line.split() for line in sys.stdin)
    number_of_variables = [int(i) for i in next(reader)]  # Количество команд
    for number in range(*number_of_variables):
        comand = next(reader)
        if comand[0] == 'add':
            phone_book[comand[1]] = comand[2]
        elif comand[0] == 'find':
            print(phone_book.get(comand[1], 'not found'))
        elif comand[0] == 'del':
            phone_book.pop(comand[1], 'not found')


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()#verbose=True
    main()