#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints elements form.

    Args:
        my_list: list of elem.
        x: The number of elem to print.

    Returns:
        the number of elem printed.
    """
    beg = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            beg += 1
        except IndexError:
            break
    print("")
    return (beg)
