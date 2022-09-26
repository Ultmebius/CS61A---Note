# Prime factorization
from tkinter import N


def prime_factors(n):
    while n > 1:
        t = smallest_factors(n)
        n = n / t
        print(t)
        
    
def smallest_factors(n):
    t = 2
    while n % t != 0:
        t = t + 1
    return t

# 
def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

from operator import mul

def pi_term(k):
    return 8 / mul(k * 4 - 3, k * 4 - 1)

def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total 
