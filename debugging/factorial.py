#!/usr/bin/python3
import sys

def factorial(n):
    if not isinstance(n, int) or n < 0:
        return None  # Return None for invalid inputs
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid infinite loop
    return result

try:
    f = factorial(int(sys.argv[1]))
    if f is None:
        print("Error: Please provide a non-negative integer")
    else:
        print(f)
except (IndexError, ValueError):
    print("Error: Please provide a valid integer argument")
