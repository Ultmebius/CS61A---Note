from regex import P
from sympy import false


def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    return temp < 60 or raining

def nearest_ten(n):
    """
    >>> nearest_ten(0)
    0
    >>> nearest_ten(4)
    0
    >>> nearest_ten(5)
    10
    >>> nearest_ten(61)
    60
    >>> nearest_ten(2023)
    2020
    """
    "*** YOUR CODE HERE ***"
    assert n >= 0
    if (n == 0 or n % 10 == 0):
        return n
    elif (n % 10 < 5):
        return n // 10 * 10
    else:
        return n + (10 - n % 10)
    
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    c = 2
    if (n == 1):
        return false
    while (c < n):
        if(n % c == 0 ):
            return false
        c += 1
    return True
    
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result is None  # No return value
    True
    """
    "*** YOUR CODE HERE ***"
    i = 1
    while(i <= n):
        if (i % 3 == 0 and i % 5 == 0):
            print("fizzbuzz")
        elif(i % 3 == 0):
            print("fizz")
        elif(i % 5 == 0):
            print("buzz")
        else:
            print(i)
        i += 1