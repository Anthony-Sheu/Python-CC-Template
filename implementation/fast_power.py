def fast_power(base, power):
    MOD = int(1e9 + 7)
    result = 1
    while power > 0:
        if power % 2 == 1:
            result *= base % MOD
        power //= 2
        base *= base % MOD
    return result
