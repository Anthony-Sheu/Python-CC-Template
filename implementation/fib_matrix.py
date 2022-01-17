def fib(n):  # the a value is the nth fib number and MOD is 1e9+7
    # Courtesy of Little_Mouse (Tommy Shan)
    if n == 1: return 1, 1, 0
    a, b, c = fib(n//2)
    a, b, c = (pow(a, 2)+pow(b, 2))%MOD,(a*b+b*c)%MOD,(pow(b, 2)+pow(c, 2))%MOD
    if n%2 == 1: a, b, c = (a+b)%MOD, a, b
    return a, b, c  # a is the n'th fib value
