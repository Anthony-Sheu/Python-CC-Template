def Sieve(n):
    prime = emp(1, n+1)  # 0 for composite, 1 for prime
    i = 2
    prime[0] = prime[1] = 0
    while i*i <= n:
        if prime[i]:
            for _ in range(i*i, n+1, i): prime[_] = 0
        i += 1
    return prime

def SegmentedSieve(n):
    lim = int(__import__("math").sqrt(n)+1)
    Sieve(lim)  # primes up to sqrt(n)
    lo, hi = lim, lim*2
    while lo < n:
        if hi >= n: hi = n
        prime = emp(1, n+1)
        for i in range(n):
            lolim = int(__import__('math').floor(lo / prime[i])*prime[i])
            if lolim < lo: lolim += prime[i]
            for j in range(lolim, hi, prime[i]): prime[j-lo] = 0
        for i in range(lo, hi): 
            if prime[i-lo]: print(i)
        lo += lim
        hi += lim
