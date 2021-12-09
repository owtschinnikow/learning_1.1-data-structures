"""
Sample Input 1:
aba
abacaba

Sample Output 1:
0 4

Sample Input 2:
Test
testTesttesT

Sample Output 2:
4

Sample Input 3:
aaaaa
baaaaaaa

Sample Output 3:
1 2 3
"""

import sys


"""
number_p = 1000000007
number_x = 263
"""


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

    """
    hash_table = [[]*i for i in range(*size_spreadsheet)]
    for number in range(*number_of_variables):
        comand = next(reader)

        if comand[0] == 'add':
            hash_cell = made_hash(comand[1], size_spreadsheet)
            if comand[1] not in hash_table[hash_cell - 1]:
                hash_table[hash_cell - 1].append(comand[1])

        elif comand[0] == 'check':
            if hash_table[int(comand[1])- 1]:
                print( *hash_table[int(comand[1]) - 1][::-1])
            else:
                print()

        elif comand[0] == 'find':
            hash_cell = made_hash(comand[1], size_spreadsheet)
            if comand[1] not in hash_table[hash_cell - 1]:
                print('no')
            else:
                print('yes')

        elif comand[0] == 'del':
            hash_cell = made_hash(comand[1], size_spreadsheet)
            if comand[1] in hash_table[hash_cell - 1]:
                hash_table[hash_cell - 1].remove(comand[1])
    """

if __name__ == '__main__':
    # import doctest
    # doctest.testmod()#verbose=True
    main()