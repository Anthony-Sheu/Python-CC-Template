# Python template by Anthony Sheu #
import sys
import collections
import bisect
import math
# sys.setrecursionlimit(1000000)  # comment this out if you are getting memory error on pypy3
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
all_data = lambda: sys.stdin.read().split('\n')
printf = lambda x: sys.stdout.write("%d\n" % x)  # comment out when using py2
prints = lambda x: sys.stdout.write(x)
printline = lambda x: list(map(print, x))
printeach = lambda x, y="": print(*x, sep=y)  # x is iterable and y is separator, also comment out when using py2
gi = lambda: list(map(int, readline().split()))
gs = lambda: readline().strip().split()
emp = lambda x, y: [x] * y  # only use for 1d arrays
fill = lambda x: list(range(1, x + 1))
flat = lambda x, l: x.join(map(str, l))  # " \n"[i == n] also works
mat, mit, MOD = sys.maxsize, -sys.maxsize, int(1e9 + 7)
######################## End of Template #######################
