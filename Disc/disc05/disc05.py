# Q1: Map, Filter, Reduce
def my_map(fn, seq):
    """Applies fn onto each element in seq and returns a list.
    >>> my_map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    """
    "*** YOUR CODE HERE ***"
    return [fn(x) for x in seq]

def my_filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred.
    >>> my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])  # new list has only even-valued elements
    [2, 4]
    """
    "*** YOUR CODE HERE ***"
    return [x for x in seq if pred(x)]

def my_reduce(combiner, seq):
    """Combines elements in seq using combiner.
    seq will have at least one element.
    >>> my_reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 1 + 2 + 3 + 4
    10
    >>> my_reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 1 * 2 * 3 * 4
    24
    >>> my_reduce(lambda x, y: x * y, [4])
    4
    >>> my_reduce(lambda x, y: x + 2 * y, [1, 2, 3]) # (1 + 2 * 2) + 2 * 3
    11
    """
    "*** YOUR CODE HERE ***"
    if len(seq) == 1:
        return seq[0]
    return combiner(seq[-1], my_reduce(combiner, seq[:-1]))

# Q2: Count Palindromes
def count_palindromes(L):
    """The number of palindromic strings in the sequence of strings
    L (ignoring case).
    >>> count_palindromes(("Acme", "Madam", "Pivot", "Pip"))
    2
    >>> count_palindromes(["101", "rAcECaR", "much", "wow"])
    3
    """
    return len([x for x in L if x.lower() == x[::-1].lower()])

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

'''
# Q3: Tree Abstraction Barrier

# Consider a tree t constructed by calling tree(1, [tree(2), tree(4)]). 
# For each of the following expressions, answer these two questions:
# What does the expression evaluate to?
# Does the expression violate any abstraction barriers? If so, write an equivalent expression that does not violate abstraction barriers.

t = tree(1, [tree(2), tree(4)])

>>> label(branches(t)[0])
2
# This expression evaluates to the label of the first branch of `t`.
# It is not a violation to index into `branches(t)` because it is
# given in the description of the ADT that `branches(t)` returns a
# list of branches.

>>> branches(tree(5, [t, tree(3)]))[0][0]
1

# This expression evaluates to the label of the tree `t`, which is 1.
# This is because the expression `tree(5, [t, tree(3)])` evaluates to
# a tree whose first branch is the tree `t` that we constructed above!
# Howvever, this expression violates the abstraction barrier by
# indexing into `t` to get its label. An equivalent expression would
# be `label(branches(tree(5, [t, tree(3)]))[0])`.
'''

def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    >>> t = tree(3, [tree(1), tree(2, [tree(5, [tree(6)]), tree(1)])])
    >>> height(t)
    3
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return 0
    else:
        return 1 + max([height(branch) for branch in branches(t)])

def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return label(t)
    else:
        return max([label(t) + max_path_sum(branch) for branch in branches(t)])

def find_path(t, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if x == label(t):
        return [label(t)]
    for branch in branches(t):
        path = find_path(branch, x)
        if path:
            return [label(t)] + path #不会