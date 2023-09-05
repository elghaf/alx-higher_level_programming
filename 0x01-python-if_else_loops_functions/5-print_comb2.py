#!/usr/bin/python3
for index_u in range(0, 100):
    if index_u == 99:
        print("{}".format(index_u))
    else:
        print("{:02}".format(index_u), end=", ")
