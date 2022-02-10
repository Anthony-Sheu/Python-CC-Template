def Sieve(n):
    prime = emp(1, n+1)  # 0 for composite, 1 for prime
    i = 2
    prime[0] = prime[1] = 0
    while i*i <= n:
        if prime[i]:
            for _ in range(i*i, n+1, i): prime[_] = 0
        i += 1
    return prime
