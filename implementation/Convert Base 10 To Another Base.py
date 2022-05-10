def bb(base, num):
    res = ""
    while num >= base:
        res = repr(num%base) + res
        num //= base
    if num: res = repr(num) + res
    if not res: res = 0
    return int(res)
