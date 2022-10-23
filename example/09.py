#Tree Recursion

def cascade(n):
    """Print a cascade of prefixes of n."""
    if n < 10:
        print(n)
    elif n > 10:
        print(n)
        cascade(n // 10)
        print(n)
        
def cascade2(n):
    """Print a cascade of prefixes of n."""
    print(n)
    if n >= 10:
        cascade2(n // 10)
        print(n)
        
def inverse_cascade(n):
    """Print an inverse cascade of prefixes of n. inverse_cascade(n)."""
    grow(n)
    print(n)
    shrink(n)
    
def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)
        
grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)

def fib(n):
    """Compute the nth Fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fib(n - 2) + fib(n - 1)
    
def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks."""
    
    if n == 1:
        print_move(start, end)
    else:
        assert 1 <= start <= 3 and 1 <= end <= 3 and start != end
        sqare_peg = 6 - start - end
        move_stack(n - 1, start, sqare_peg)
        print_move(start, end)
        move_stack(n -1, sqare_peg, end)
        
def count_partitions(n, m):
    """Count the partitions of n using parts up to size m.
    复制粘贴的，懒得写了······
    >>> count_partitions(6, 4)
    9
    >>> count_partitions(10, 10)
    42
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m