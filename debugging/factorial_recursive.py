#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
        Recursively computes the factorial of a non-negative integer.

    Parameters:
        n (int): A non-negative integer whose factorial will be computed.

    Returns:
        int: The factorial of n (n!), with 0! defined as 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
