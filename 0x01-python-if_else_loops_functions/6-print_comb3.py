#!/usr/bin/python3
# 6- print all combinations

for index_i in range(0, 10):
    for index_j in range(index_i + 1, 10):
        if index_i == 8 and index_j == 9:
            print("{}{}".format(index_i, index_j))
        else:
            print("{}{}".format(index_i, index_j), end=", ")
