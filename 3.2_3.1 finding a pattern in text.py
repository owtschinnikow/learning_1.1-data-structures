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


def made_hash(text):
    """
    Function made hash key wich size_spreadsheet for the text.
    :param text:
    :param size_spreadsheet:
    :return:
    """
    hash_key = 0
    for number, ascii in enumerate(to_ascii(text)):
        hash_key += ((ascii * (number_x ** number)) % number_p)
    return (hash_key % number_p)



def main():
    """
    Function processes the input to the program and runs the desired functions.
    :return:
    """
    reader = (line.split() for line in sys.stdin)
    pattern = next(reader)[0]  # Pattern
    text = next(reader)[0]  # Text
    hash_pattern = made_hash(pattern)

    for index, character in enumerate(text):
        if index < len(text) - len(pattern)+1:
            hash_pattern_in_text = made_hash(text[index : index + len(pattern)])
            if hash_pattern == hash_pattern_in_text:
                print(index, end=' ')


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()#verbose=True
    main()