# Tree Recursion

# Tree

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


### +++ === ABSTRACTION BARRIER === +++ ###

def fib_tree(n):
    """Construct a Fibonacci tree.
    
    >>> fib_tree(1)
    [1]
    >>> fib_tree(3)
    [2, [1], [1, [0], [1]]]
    >>> fib_tree(5)
    [5, [2, [1], [1, [0], [1]]], [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]]
    """
    if n == 0 or n == 1:
        return tree(n)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])


def count_leaves(t):
    """The number of leaves in tree.

    >>> count_leaves(fib_tree(5))
    8
    """
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])
