from string import digits
from unicodedata import digit


def remove(n, digit):
    kept, digits = 0, 0
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept = kept + 1
            digits = digits + last * pow(10, (kept - 1))
    return digits

# Decorators


def trace1(fn):
    def traced(x):
        print("Calling", fn, "Argument", x)
        return fn(x)
    return traced


@trace1
def square(x):
    return x * x


@trace1
def sum_squares_up_to(n):
    totlal, k = 0, 1
    while k <= n:
        totlal, k = totlal + square(k), k + 1
    return totlal

