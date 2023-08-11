#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    """
    - If the number of arguments is not 3,
    your program has to:
    - print Usage: ./100-my_calculator.py <a> <operator> <b>
    followed with a new line
    - exit with the value 1
    """
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    """
    operator can be:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    """
        ops = {"+": add, "-": sub, "*": mul, "/": div}
        if sys.argv[2] not in list(ops.keys()):
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
