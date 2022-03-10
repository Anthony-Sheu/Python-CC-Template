import sys
sys.setrecursionlimit(100000) 

def read(dp, a, b, la, lb):
    if not la or not lb: return ""
    elif a[la-1] == b[lb-1]: return read(dp, a, b, la-1, lb-1)+a[la-1]
    elif dp[la-1][lb] > dp[la][lb-1]: return read(dp, a, b, la-1, lb)
    return read(dp, a, b, la, lb-1)

def LCS(a, b):
    dp = [[0 for i in range(len(b)+1)] for i in range(len(a)+1)]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]: dp[i][j] = dp[i-1][j-1]+1
            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return read(dp, a, b, len(a), len(b))

a, b = "axyb", "abyxb"
print(LCS(a, b))
