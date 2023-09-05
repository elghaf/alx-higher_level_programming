#!/usr/bin/python3
# 102- magic calculation


def magic_calculation(a, b, c):
    """magic calculation a,b,c"""
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)
