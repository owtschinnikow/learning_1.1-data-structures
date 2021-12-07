"""
Sample Input 1:
5
12
add world
add HellO
check 4
find World
find world
del world
check 4
del HellO
add luck
add GooD
check 2
del good

Sample Output 1:
HellO world
no
yes
HellO
GooD luck

Sample Input 2:
4
8
add test
add test
find test
del test
find test
find Test
add Test
find Test

Sample Output 2:
yes
no
no
yes
"""

import sys




def to_ascii(text):
    """
    Function changes characters to ascii code
    :param text:
    :return: 
    """
    ascii_values = [ord(character) for character in text]
    return ascii_values


def main():
    """
    Функция обрабатывает ввод в программу, запускает нужные функции
    :return:
    """
    reader = (line.split() for line in sys.stdin)
    size_spreadsheet = [int(i) for i in next(reader)]  # Size of spreadsheet
    number_of_variables = [int(i) for i in next(reader)]  # Количество команд
    for number in range(*number_of_variables):
        print(next(reader))

        # comand = next(reader)
        # if comand[0] == 'add':
        #     phone_book[comand[1]] = comand[2]
        # elif comand[0] == 'find':
        #     print(phone_book.get(comand[1], 'not found'))
        # elif comand[0] == 'del':
        #     phone_book.pop(comand[1], 'not found')

    print(to_ascii('world'))




if __name__ == '__main__':
    # import doctest
    # doctest.testmod()#verbose=True
    main()
