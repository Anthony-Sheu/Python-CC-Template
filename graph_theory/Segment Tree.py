def build(v, l, r):
    if l == r: seg[v] = arr[l]; return arr[l]
    mid = l+(r-l)//2
    seg[v] = min(build(v*2, l, mid), build(v*2+1, mid+1, r))
    return seg[v]

def query(l, r, tl, tr, v):
    if l == tl and r == tr: return seg[v]
    mid = l+(r-l) // 2
    if tr <= mid: return query(l, mid, tl, tr, 2 * v)
    elif mid < tl: return query(mid+1, r, tl, tr, 2 * v+1)
    else: return min(query(l, mid, tl, mid, 2 * v), query(mid + 1, r, mid + 1, tr, 2 * v + 1))

def update(pos, val, num, l, r):
    if l == pos and r == pos: seg[num] = val; return
    mid = (l + r)//2
    if pos <= mid: update(pos, val, 2 * num, l, mid)
    else: update(pos, val, 2 * num+1, mid+1, r)
    seg[num] = min(seg[2 * num], seg[2 * num+1])
