# Sequence

# List

odds = [41, 43, 47, 49]

#Containers

digits = [1, 8, 2, 8]

# For statements

def count_for(s, value):
    """Count the number of occurrences of value in sequence s.

    >>> count_while(digits, 8)
    2
    """
    total = 0
    for i in s:
        if i == value:
            total = total + 1
    return total

def count_same(pairs):
    """Return how many pairs have the same element repeated.

    >>> pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
    >>> count_same(pairs)
    2
    """
    total = 0
    for x, y in pairs:
        if x == y:
            total += 1
    return total

# Range

def sum_below(n):
    total = 0
    for i in range(n):
        total = total + i
    return total

def cheer(n):
    for _ in range(n):
        print('Go Bears!')
        
# List comprehensions

def divisors(n):
    """Return the integers that evenly divide n.

    >>> divisors(1)
    [1]
    >>> divisors(4)
    [1, 2]
    >>> divisors(12)
    [1, 2, 3, 4, 6]
    >>> [n for n in range(1, 1000) if sum(divisors(n)) == n]
    [1, 6, 28, 496]
    """
    return [1] + [i for i in range(2, n) if n % i == 0]

def odds(x):
    return x % 2 == 1

def promoted(s, f):
    """Return a list with the same elements as s, but with all
    elements e for which f(e) is a true value placed first.

    >>> promoted(range(10), odd)  # odds in front
    [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    """
    
    return [n for n in s if f(n)] + [n for n in s if not f(n)]