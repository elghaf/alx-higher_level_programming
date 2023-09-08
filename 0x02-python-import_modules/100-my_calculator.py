#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculation_1 import add, sub, mul, div

    arguments = sys.argv[1:]

    argument_count = len(arguments)

    operators = ["+", "-", "*", "/"]

    if argument_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    elif arguments[1] not in operators:
        exit(1)

    else:
        num1 = int(arguments[0])
        num2 = int(arguments[2])

        if arguments[1] == "+":
            print("{:d} + {:d} = {:d}".format(num1, num2, add(num1, num2)))

        elif arguments[1] == "-":
            print("{:d} - {:d} = {:d}".format(num1, num2, sub(num1, num2)))

        elif arguments[1] == "*":
            print("{:d} * {:d} = {:d}".format(num1, num2, mul(num1, num2)))

        elif arguments[1] == "/":
            print("{:d} / {:d} = {:d}".format(num1, num2, div(num1, num2)))
