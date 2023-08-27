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
    if n % 10 < 5:
        return n // 10 * 10
    else:
        return (n // 10 + 1) * 10

#Alternate Solution
def nearest_ten(n):
    return (n + 5) // 10 * 10