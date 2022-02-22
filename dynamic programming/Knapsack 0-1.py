n, m = gi()  # number of elements, max weight
dp = emp(0, m+1)
arr = [gi() for i in range(n)]  # value, weight 
for i in range(n):
    for j in range(m, arr[i][1] - 1, -1): dp[j] = max(dp[j], arr[i][0] + dp[j - arr[i][1]])
printf(dp[m])
