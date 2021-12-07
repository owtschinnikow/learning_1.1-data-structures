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


number_p = 1000000007
number_x = 263



def to_ascii(text):
    """
    Function changes characters to ascii code
    :param text:
    :return: 
    """
    ascii_values = [ord(character) for character in text]
    return ascii_values


def made_hash(text, size_spreadsheet):
    """
    Function made hash key wich size_spreadsheet for the text.
    :param text:
    :param size_spreadsheet:
    :return:
    """
    hash_key = 0
    for number, ascii in enumerate(to_ascii(text)):
        hash_key += ((ascii * (number_x ** number)) % number_p)
    return ((hash_key % number_p) % size_spreadsheet[0])



def main():
    """
    Function processes the input to the program and runs the desired functions.
    :return:
    """
    reader = (line.split() for line in sys.stdin)
    size_spreadsheet = [int(i) for i in next(reader)]  # Size of spreadsheet
    number_of_variables = [int(i) for i in next(reader)]  # Количество команд
    for number in range(*number_of_variables):
        print(next(reader))

    print(to_ascii('world'))

    print(made_hash('world', size_spreadsheet))
    print(made_hash('HellO', size_spreadsheet))

"""
    hash_key = 0

    for number, ascii in enumerate(to_ascii('world')):
        print(number, ascii)
        hash_key += ((ascii * (number_x ** number)) % number_p)
        print(hash_key)
    print((hash_key % number_p) % size_spreadsheet[0])
"""


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()#verbose=True
    main()
