def fib_matrix():
    a, b = 0, 1
    for _ in bin(readint()%2000000016)[2:]:
        if _ == '1':
            temp = (a*((2*b)-a))%MOD
            b = (a*a+b*b)%MOD
            a = temp
            temp = b
            b = (a+b)%MOD
            a = temp
        else: a, b = (a*(2*b-a))%MOD, (a*a+b*b)%MOD
    return a
