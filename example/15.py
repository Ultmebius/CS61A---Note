# Syntax

# Trees

import string
from string import punctuation


def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)


def label(t):
    return t[0]


def branches(t):
    return t[1:]


def is_tree(t):
    if type(t) != list or len(t) < 1:
        return False
    for branch in branches(t):
        if not is_tree(branch):
            return False
    return True


def is_leaf(t):
    return not branches(t)


def leaves(t):
    """Return a list of the leaf labels of a tree."""
    if is_leaf(t):
        return [label(t)]
    else:
        return sum([leaves(b) for b in branches(t)], [])


# Syntax

example = tree('FRAG',
               [tree('NP',
                     [tree('DT', [tree('a')]),
                      tree('JJ', [tree('little')]),
                      tree('NN', [tree('bug')])]),
                tree('.', [tree('.')])])

tree('NP',[tree('DT', [tree('a')])])
