def fast_power(base, power):
    MOD = int(1e9 + 7)
    result = 1
    while power > 0:
        if power % 2 == 1:
            result *= base % MOD
        power //= 2
        base *= base % MOD
    return result
#####################################
def qpow(base, exp):
    if not exp: return 1
    x = qpow(base, exp>>1)
    x *= x
    if exp%2: x *= base
    return x
#####################################
def qpow(base, exp, mod):
    if not base: return 0
    if not exp: return 1
    if not exp%2:
        res = qpow(base, exp//2, mod)
        res = (res * res) % mod
    else:
        res = base % mod
        res = (res * qpow(base, exp-1, mod) % mod) % mod
    return (res + mod) % mod
#####################################
def qpow(base, exp, mod):
    res = 1
    base %= mod
    if not base: return 0
    while exp > 0:
        if exp & 1 == 1: res *= base % mod
        exp >>= 1
        base *= base % mod
    return res
