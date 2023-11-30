#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mult, div
    argv = sys.argv[1:]
    argv_count = len(argv)
    operators = ["+", "-", "*", "/"]
    if argv_count != 3:
        print("Usage: ./100-my_calculator.py <x> <operator> <y>")
        exit(1)
    elif sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        x = int(sys.argv[1])
        y = int(sys.argv[3])
        if sys.argv[2] == "+":
            print("{:d} + {:d} = {:d}".format(x, y, add(x, y)))
        elif sys.argv[2] == "-":
            print("{:d} - {:d} = {:d}".format(x, y, sub(x, y)))
        elif sys.argv[2] == "*":
            print("{:d} * {:d} = {:d}".format(x, y, mul(x, y)))
        elif sys.argv[2] == "/":
            print("{:d} / {:d} = {:d}".format(x, y, div(x, y)))
