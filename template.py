import sys

def swap(x, y, arr): arr[x], arr[y] = arr[y], arr[x]

def gcd(x, y):
    if not x: return y
    return gcd(y % x, x)

def lcm(x, y): return x // gcd(x, y) * y

def prime(n):
    arr = []
    while not n % 2: n //= 2; arr.append(2)
    i, f = 3, n
    while 1:
        if pow(i, 2)+1 >= f: break
        while not n % i: n //= i; arr.append(i)
        i += 2
    if n > 2: arr.append(n)
    return arr

def kmp(txt, pat):
    m, n = len(pat), len(txt)
    lps, i, j, l, k = [0] * m, 0, 0, 0, 1
    while k < m:
        if pat[k] == pat[l]: l += 1; lps[k] = l; k += 1
        else:
            if l: l = lps[l - 1]
            else: lps[k] = 0; k += 1
    while i < n:
        if pat[j] == txt[i]: i += 1; j += 1
        if j == m: return i - j
        elif i < n and pat[j] != txt[i]:
            if j: j = lps[j - 1]
            else: i += 1
    return -1

readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
printf = lambda x: sys.stdout.write(f"{x}\n")
prints = lambda x, y=None: sys.stdout.write(x + y)
printline = lambda x: list(map(printf, x))
printeach = lambda x, y=None: print(*x, sep=y)  # x is iterable and y is separator
gi = lambda: list(map(int, readline().split()))
gs = lambda: readline().strip().split()
emp = lambda x: [0]*x
fill = lambda x: list(range(1, x+1))
flat = lambda x, l: x.join(map(str, l))  # " \n"[i == n] also works

max_int, min_int = float('inf'), float('-inf')
MOD = int(1e9+7)
######################## End of Template #######################
