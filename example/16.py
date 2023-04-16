#iterator

s = [[1, 2], 3, 4, 5]
t = iter(s)
u = iter(s)
d = {'one': 1, 'two': 2, 'three': 3}
k = iter(d)
v = iter(d.values())
k = iter(d)
r = range(3, 6)
l = iter(r)

def double(x):
    print('***', x, '=>', 2 * x, '***')
    return 2 * x

