def miller(i):  # prime test 0 for composite and 1 for prime
    if i == 1 or i == 4: return 0
    if i <= 3: return 1
    d = i-1
    while not d%2: d //= 2
    for j in range(10):
        if not calc(d, i): return 0
    return 1

def calc(d, i):
    a = 2 + __import__("random").randint(1, i - 4)
    x = power(a, d, i)
    if x == 1 or x == i - 1: return 1
    while d != i - 1:
        x = (x * x) % i
        d *= 2
        if x == 1: return 0
        if x == i - 1: return 1
    return 0

def power(x, y, p):
    res = 1
    x %= p
    while y:
        if y & 1:
            res = (res * x) % p
        y >>= 1
        x = (x * x) % p
    return res
