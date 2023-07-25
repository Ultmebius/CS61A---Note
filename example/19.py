#Representation


from fractions import Fraction


def str_repr_demo():
    from fractions import Fraction
    half = Fraction(1, 2)
    s = "hello world"
    repr(repr(repr(s)))
    eval(eval(eval(repr(repr(repr(s)))))) 


class Bear:
    """A Bear.
    
    
    >>> oski = Bear()
    >>> oski
    Bear()
    >>> print(oski)
    a bear
    >>> print(str(oski))
    a bear
    >>> print(repr(oski))
    Bear()
    >>> print(oski.__repr__())
    oski
    >>> print(oski.__str__())
    oski the bear

    >>> print(str_(oski))
    a bear
    >>> print(repr_(oski))
    Bear()
    """
    def __init__(self):
        self.__repr__ = lambda:  'oski'
        self.__str__ = lambda: 'oski the bear'
        
    def __repr__(self):
        return 'Bear()'
    
    def __str__(self):
        return 'a bear'
    
    
    