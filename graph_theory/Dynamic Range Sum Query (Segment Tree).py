def build(v, l, r, seg, arr):
    if l == r: seg[v] = arr[l]; return arr[l]
    mid = l+(r-l)//2
    seg[v] = build(v*2, l, mid, seg, arr) + build(v*2+1, mid+1, r, seg, arr)
    return seg[v]

def query(l, r, tl, tr, v, seg):
    if l == tl and r == tr: return seg[v]
    mid = l+(r-l) // 2
    if tr <= mid: return query(l, mid, tl, tr, 2 * v, seg)
    elif mid < tl: return query(mid+1, r, tl, tr, 2 * v+1, seg)
    else: return query(l, mid, tl, mid, 2 * v, seg) + query(mid + 1, r, mid + 1, tr, 2 * v + 1, seg)

def update(pos, val, num, l, r, seg):
    if l == pos and r == pos: seg[num] = val; return
    mid = (l + r)//2
    if pos <= mid: update(pos, val, 2 * num, l, mid, seg)
    else: update(pos, val, 2 * num+1, mid+1, r, seg)
    seg[num] = seg[2 * num] + seg[2 * num+1]
