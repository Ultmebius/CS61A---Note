# Prime factorization
def prime_factors(n):
    while n > 1:
        t = smallest_factors(n)
        n = n / t
        print(t)
        
    
def smallest_factors(n):
    t = 2
    while n % t != 0:
        t = t + 1
    return t

# DRY
