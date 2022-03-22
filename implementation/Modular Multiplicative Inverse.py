def modInverse(a, m):
    m1, y, x = m, 0, 1
    if m == 1: return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0: x += m1
    return x

# printf(modInverse(2, 7)) answer is 4
