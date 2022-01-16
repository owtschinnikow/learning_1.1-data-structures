"""
Sample Input 0:
aba
abacaba

Sample Output 0:
0 4

Sample Input 1:
Test
testTesttesT

Sample Output 1:
4

Sample Input 2:
aaaaa
baaaaaaa

Sample Output 2:
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
    return hash_key % number_p


def made_hash_refresh(hash_key_old, old_char, new_char):
    hash_key = hash_key_old - ord(old_char) + ord(new_char)
    return ((hash_key + number_p) % number_p)


def made_hash_refresh_2(hash_key_old, old_char, new_char):

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
                if pattern == text[index:index + len(pattern)]:
                    print(index, end=' ')
            hash_pattern_in_text = made_hash_refresh_2(hash_pattern_in_text,
                                                   _character,
                                                    text[index + len(pattern) - 1])


def find_all(source, sub):
    def prefix_func(s):
        pr = [0] * (len(s))
        for i in range(1, len(s)):
            k = pr[i - 1]
            while k > 0 and s[k] != s[i]:
                k = pr[k - 1]
            if s[k] == s[i]:
                k = k + 1
            pr[i] = k
        return pr

    result = prefix_func(sub + "$" + source)  # вместо доллара может быть любой другой не встречаюшийся символ
    return [index for index, element in enumerate(result) if (element >= len(sub))]

def find_all_1(s, sub):
    res = []
    cur_pos = 0
    for x in s.split(sub)[:-1]:
        cur_pos += len(x)
        res.append(cur_pos)
        cur_pos += len(sub)
    return res

def findall(s, substr):
  def searching(s, substr):
    while s.rfind(substr) != -1:
      yield s.rfind(substr)
      s = s[:s.rfind(substr)]
  return list(reversed(list(searching(s,substr))))

def main_3():
    reader = (line.split() for line in sys.stdin)
    pattern = next(reader)[0]  # Pattern
    text = next(reader)[0]  # Text

    f = findall(text, pattern)
    print(f)

def main_2():
    """
    Function processes the input to the program and runs the desired functions.
    :return:
    """
    reader = (line.split() for line in sys.stdin)
    pattern = next(reader)[0]  # Pattern
    text = next(reader)[0]  # Text

    index = text.find(pattern)
    print(index)



if __name__ == '__main__':
    # import doctest
    # doctest.testmod()#verbose=True
    # main()
    main_3()