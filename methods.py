#  Code created by Anthony Sheu on 9/11/21, 8:32 PM
#####################################
def gcd(x, y):
    if not y: return x
    return gcd(y, x % y)
###################################
def lcm(x, y):
    return x // gcd(x, y) * y
###################################
MOD = int(1e9+7)
def fast_power(base, power):
    global MOD
    result = 1
    while power > 0:
        if power % 2 == 1:
            result *= base % MOD
        power //= 2
        base *= base % MOD
    return result
###################################
def getCombo(i, n, arr=[]):  # i must always be 1, n is the number of numbers
    if i > n: return
    getCombo(i+1, n, arr)
    arr.append(i)
    getCombo(i+1, n, arr)
    arr.pop(len(arr)-1)

# getCombo(1, 3, [])
######################################
def hanoi(n, a, b, c):
    if n == 1:
        print(a + "-->" + c)
        return
    hanoi(n-1, a, c, b)
    print(a + "-->" + c)
    hanoi(n-1, b, a, c)

# hanoi(4, "A", "B", "C")
######################################
def next_permutation(a):
    if len(a) <= 1: return 0
    p = len(a) - 2; q = len(a) - 1
    while p >= 0 and a[p] >= a[p + 1]: p -= 1
    if p < 0: return 0
    while a[q] <= a[p]: q -= 1
    temp = a[p]; a[p] = a[q]; a[q] = temp
    l, r = p+1, len(a)-1
    while l < r:
        temp = a[l];  a[l] = a[r]; a[r] = temp
        l += 1; r -= 1
    return a

# r = next_permutation([1, 2, 3, 4])
# for i in range(20):
#     print(next_permutation(r))
######################################
# def queen(r):
#     if r == n:
#         print("=" * (n + 2))
#         for i in range(n):
#             for j in range(n):
#                 print("Q", end="") if j == row[i] else print(".", end="")
#             print()
#
#     for i in range(n):
#         if not col[i] and not left[r+i] and not right[r+n-1-i]:
#             row[r] = i
#             col[i] = left[r+i] = right[r+n-1-i] = 1
#             queen(r+1)
#             col[i] = left[r+i] = right[r+n-1-i] = 0


# n = int(input())
# row = [0] * n
# col, left, right = [0] * n, [0] * (2*n-1), [0] * (2*n-1)
# queen(0)
############################################################
def prime(n):
    arr = []
    while not n % 2: n //= 2; arr.append(2)
    i = 3
    temp = n
    while n > 2:
        if pow(i, 2)+1 >= temp: break
        while not n % i: n //= i; arr.append(i)
        i += 2
    arr.append(n) if n > 2 else None
    return arr
#########################################################
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
##########################################################
def swap(x, y, arr): arr[x], arr[y] = arr[y], arr[x]
##########################################################