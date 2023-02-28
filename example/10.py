#Data Abstraction2

from re import X


def add_rational(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return (nx * dy + ny * dx, dy * dx)

def mul_rational(x, y):
    """The product of rational numbers X and Y."""
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def rationals_are_equal(x, y):
    """True iff rational numbers X and Y are equal."""
    return numer(x) * denom(y) == numer(y) * denom(x)

def print_rational(x):
    print(numer(x), "/", denom(x))
    
def rational(n, d):
    return [n, d]

def numer(x):
    return x[0]

def denom(x):
    return x[1]

a = [1, 2]
b = [3, 4]
print_rational(add_rational(a, b))
    
