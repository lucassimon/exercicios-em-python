# -*- coding: utf-8 -*-


def is_balanced(value):
    if not value:
        return False

    pairs = [('(', ')'), ('[', ']'), ('{', '}')]

    stack = []

    for char in value:
        for pair in pairs:

            if char == pair[0]:
                stack.append(char)
                continue

            elif (
                char == pair[1] and
                (
                    len(stack) == 0 or
                    stack.pop() != pair[0]
                )
            ):
                return False

    expected = [i[1] for i in pairs if stack and stack[0] == i[0]]

    if expected:
        print '\nExpression: {} Expected: {}'.format(value, expected[0])

    if len(stack) == 0:
        return True

    return False


if __name__ == '__main__':

    print is_balanced('')

    print is_balanced('(){}[]')

    print is_balanced('[{()}](){}')

    print is_balanced('[]{()')

    print is_balanced('[{)]')

    print is_balanced('[[](){}[]]')

    print is_balanced('test)')

    print is_balanced('(te{}st)')

    print is_balanced('[(){}]]')

    print is_balanced('[(]{)}')

    print is_balanced('[({})]')

    print is_balanced('[](){}')

    print is_balanced('(())')

    print is_balanced(')(')

    print is_balanced('()')

    print is_balanced('(')

    print is_balanced('(A+B)')

    print is_balanced('{(A+B) * (B+C)}')

    print is_balanced('{ (x+y) * (z)')
