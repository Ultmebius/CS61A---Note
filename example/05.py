# Functional arguments
from math import degrees


def square_twice(f, x):
    return f(f(x))

def square(x):
     return x * x

square_twice = square_twice(square, 2)

# Functional return values
def make_adder(n):
    def adder(k):
        return k + n
    return adder

adder_three = make_adder(3)
print(adder_three(4))

# Lambda expressions
square = lambda x : x * x
x = 10
print(square(x))

# Composition
def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

def triple(x):
    return 3 * x
c1 = compose1(square, triple)
c2 = compose1(triple, make_adder(7))
c3 = compose1(triple, square)

# Self Reference
def print_all(x):
    print(x)
    return print_all

def print_sumall(x):
    print(x)
    def summall(k):
        return print_sumall(k + x)
    return summall

# Currying
from operator import add, mul 

def curry2(f):
    def h(x):
        def g(y):
            return f(x, y)
        return g
    return h

m = curry2(compose1)
a = m(triple)
b = a(square)
