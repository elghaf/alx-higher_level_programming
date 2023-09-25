#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elem of list provided.

    Args:
        my_list: list of elem.
        x: The number of elem to print.

    Returns:
        The number of elements printed.
    """
    beg = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            beg += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (beg)
