def sieve_rangesum(n):
    prime = emp(0, 100001)  # set 100001 to the max bounds
    dp = emp(0, 100001)  # use dp as PSA
    prime[1] = 1; prime[0] = 1
    i = 2
    while pow(i, 2) < n+1:
        if not prime[i]:
            for j in range(pow(i, 2), n + 1, i):
                prime[j] = 1
        i += 1
    r = 0
    for i in range(1, n + 1):
        if not prime[i]:
            r += i
        dp[i] = r
