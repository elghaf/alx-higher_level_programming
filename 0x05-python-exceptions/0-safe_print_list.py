#!/usr/bin/python3
def safe_print_list(listo=[], cost = 0):
    begining = 0
    for beg in range(cost):
        try:
            print(listo[beg], end="")
            begining += 1
        except IndexError:
            break
    print()
    return begining

