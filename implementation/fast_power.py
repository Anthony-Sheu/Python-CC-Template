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
