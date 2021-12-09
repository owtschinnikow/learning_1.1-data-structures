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


def made_hash_simple(text):
    """
    Function made hash key wich size_spreadsheet for the text.
    :param text:
    :param size_spreadsheet:
    :return:
    """
    hash_key = 0
    for number, ascii in enumerate(to_ascii(text)):
        hash_key += ascii  % number_p
    return (hash_key % number_p)

def made_hash_simple_2(text):
    """
    Function made hash key wich size_spreadsheet for the text.
    :param text:
    :param size_spreadsheet:
    :return:
    """
    hash_key = 0
    for number, ascii in enumerate(to_ascii(text)):
        hash_key += ascii
    return hash_key


def made_hash_refresh(hash_key_old, old_char, new_char):
    hash_key = hash_key_old - ord(old_char) + ord(new_char)
    return ((hash_key + number_p) % number_p)


def hash_refresh_ver_2(hash_key_old, old_char, new_char):
    hash_key = hash_key_old - ord(old_char) + ord(new_char)
    return ((hash_key + number_p) % number_p)


def main():
    """
    Function processes the input to the program and runs the desired functions.
    :return:
    """
    reader = (line.split() for line in sys.stdin)
    pattern = next(reader)[0]  # Pattern
    text = next(reader)[0]  # Text

    hash_pattern = made_hash_simple_2(pattern)
    hash_pattern_in_text = made_hash_simple_2(text[0: len(pattern)])


    for index, _character in enumerate(text):
        if index < len(text) - len(pattern) + 1:
            # print(index)
            # print(hash_pattern_in_text)
            if hash_pattern == hash_pattern_in_text:
                if pattern == text[index : index + len(pattern)]:
                    print(index, end=' ')
            hash_pattern_in_text = made_hash_refresh(hash_pattern_in_text,
                                                   _character,
                                                    text[index + len(pattern) - 1])


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()#verbose=True
    main()