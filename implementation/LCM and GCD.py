def gcd(x, y):
    if not y: return x
    return gcd(y, x % y)
###################################
def lcm(x, y):
    return x // gcd(x, y) * y
