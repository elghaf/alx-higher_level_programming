#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
        my_list_1: The first list provided.
        my_list_2: The second list provided.
        list_length: The number of elements to divide.

    Returns:
        A new list of length list_length containing all the divisions.
    """
    empty_list = []
    for index in range(0, list_length):
        try:
            divided = my_list_1[index] / my_list_2[index]
        except TypeError:
            print("wrong type")
            divided = 0
        except ZeroDivisionError:
            print("division by 0")
            divided = 0
        except IndexError:
            print("out of range")
            divided = 0
        finally:
            empty_list.append(divided)
    return empty_list
