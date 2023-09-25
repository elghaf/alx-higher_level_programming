#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):    
    begining = 0
    for beg in range(x):
        try:
            print(my_list[beg], end="")
            begining += 1
        except IndexError:
            break
    print("")
    return begining

