def update(pos, val, bit, n):
    while pos < n:
        bit[pos] += val
        pos += pos & -pos

def query(pos, bit):
    s = 0
    while pos: s += bit[pos]; pos -= pos & -pos
    return s
