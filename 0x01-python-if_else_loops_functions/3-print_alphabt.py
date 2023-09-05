#!/usr/bin/python3
for index_i in range(ord('a'), ord('z') + 1):
    if index_i != ord('e') and index_i != ord('q'):
        print("{:c}".format(index_i), end="")
