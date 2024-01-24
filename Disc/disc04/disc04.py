def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)
    
def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        i = 1
        while i <= k:
            total += count_k(n-i, k)
            i += 1
        return total

"""
Q3: WWPD: Lists

>>> a = [1, 5, 4, [2, 3], 3]
>>> print(a[0], a[-1])
1 3 #是空格不是逗号

>>> 2 in a
False #大写F
"""

#Q4: Even weighted
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[i]*i for i in range(len(s)) if i % 2 == 0] #使用renge表示0到len(s)，不能直接用[0:len(s)]

#Q5: Max Product
def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s == []:
        return 1
    else:
        return max(max_product(s[1:]), s[0]*max_product(s[2:])) #使用递归很简洁

""" 
Q6: WWPD: Dictionaries
>>> pokemon[['firetype', 'flying']] = 146
unhashable type

Note that dictionaries cannot use other mutable data structures as keys. However, dictionaries can be arbitrarily deep, meaning the values of a dictionary can be themselves dictionaries.
"""


