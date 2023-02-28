# Containers

# Slicing

odds = [3, 5, 7, 9, 11]

# Aggreation

# Dict

numerals = {'I': 1, 'V': 5, 'X': 10}
numerals['X']
# numerals['X-ray']
# numerals[10]
len(numerals)
list(numerals)
numerals.values()
list(numerals.values())
sum(numerals.values())
dict([[3, 9], [4, 16]])
numerals.get('X', 0)
numerals.get('X-ray', 0)


def index(keys, values, match):
    """Return a dictionary from keys k to a list of values v for which 
    match(k, v) is a true value.

    >>> index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0)
    {7: [35, 42, 49], 9: [36, 45], 11: [33, 44]}
    """
    return {k: [v for v in values if match(k, v)] for k in keys}
