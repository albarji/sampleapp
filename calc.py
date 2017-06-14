"""
calc.py

Implements a very simple calculator
"""

def sum(a, 
  b):
    return a + b # Superarreglado!!

def sub(a, b):
    return a - b

def div(a, b):
    if b == 0:
        raise ValueError
        return 0
    return a / b

import math

def exp(a, b):
    return math.pow(a, b)

def fibonacci(i):
    if i < 0:
        raise ValueError
    if i == 0:
        return 0
    if i == 1:
        return 1
    if i == 2:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2) # Recursion to find the i-th value of fibonacci series by using the values tha are computed for smaller inputs

def factorize(i):
    factors = []
    remainder = i
    if i == 1:
        return [1]
    if i < 1:
        return ValueError
    while True:
        if remainder == 1:
            break
        # Loop over possible factors
        for f in range(2, remainder+1):
            if not remainder % f:
                factors.append(f)
                remainder = int(remainder / f)
                break
    return factors

