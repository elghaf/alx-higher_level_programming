#!/usr/bin/python3


def magic_calculation(a, b):
    list_result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                list_result += a ** b / i
        except:
            list_result = b + a
            break
    return (list_result)
