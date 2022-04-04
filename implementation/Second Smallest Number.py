def minn(numbers):
    s = set()
    sa = s.add
    un = (sa(n) or n for n in __import__('itertools').filterfalse(s.__contains__, numbers))
    return __import__('heapq').nsmallest(2, un)[-1]
