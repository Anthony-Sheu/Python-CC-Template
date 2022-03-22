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
