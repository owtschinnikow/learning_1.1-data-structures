import test_a_stack


def is_braces_sequence_correct(s: str):
    """
    Проверяет корректность скобочной последовательности
    из круглых и квадратных скобок () []

    >>> is_braces_sequence_correct("(([()]))[]")
    True
    >>> is_braces_sequence_correct("([)]")
    False
    >>> is_braces_sequence_correct("(")
    False
    >>> is_braces_sequence_correct("]")
    False
    """
    for brace in s:
        if brace not in '()[]':
            continue
        if brace in '([':
            test_a_stack.push(brace)
        else:
            assert brace in ')]', 'Ожидалась закрывающая скобка вместо:' + str(brace)
            if test_a_stack.is_empty():
                return False
            left = test_a_stack.pop()
            assert left in '([', 'Ожидалась открывающая скобка вместо:' + str(brace)
            if left == '(':
                right = ')'
            elif left == '[': #else?
                right = ']'
            if right != brace:
                return False
    return test_a_stack.is_empty()

if __name__ == '__main__':
    import doctest
    doctest.testmod()