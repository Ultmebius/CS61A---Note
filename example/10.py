#Containers 

def pair(a, b):
    def pair_func(which, v = None):
        nonlocal a, b
        if which == 0:
            return a
        elif which == 1:
            return b
        elif which == 2:
            a =v
        else:
            b = v
    return pair_func

def left(p):
    return p(0)
    
def right(p):
    return p(1)
    
def set_left(p, v):
    p(2, v)
    
def set_right(p, v):
    p(3, v)
    
def test_good_pair():
    aPair = pair(3, 2)
    set_left(aPair, 5)
    print(left(aPair))

def print_sequences():
    t = (2, 0, 9, 10, 11)   # Tuple
    L = [2, 0, 9, 10, 11]   # List
    R = range(2, 13)        # Integers 2-12.
    E = range(2, 13, 2)     # Even integers 2-12.
    S = "Hello, world!"     # Strings (sequences of characters)

    print(f"t[2] == {t[2]}; L[2] == {L[2]}; R[2] == {R[2]}; E[2] == {E[2]}")
    print(f"t[-1] == {t[-1]}' t[len(t)-1] == {t[len(t)-1]}")
    print(f"S[1] == {S[1]}")

    print(f"t[1:4] == {t[1:4]}")
    print(f"t[2:] == {t[2:]}; t[2:len(t)] == {t[2:len(t)]}")
    print(f"t[::2] == {t[::2]}; t[0:len(t):2] == {t[0:len(t):2]}; ",
          f"t[::-1] == {t[::-1]}")
    print(f"S[0:5] == {S[0:5]}; S[0:5:2] == {S[0:5:2]}; S[4::-1] == {S[4::-1]}")
    print(f"S[1:2] == {S[1:2]}; S[1] == {S[1]}")