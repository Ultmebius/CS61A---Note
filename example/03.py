from operator import  floordiv , mod 

def divide_exact (n, d = 10):
    return floordiv(n, d), mod(n, d)
 
q, r = divide_exact(2013, 10)
print(q, r)