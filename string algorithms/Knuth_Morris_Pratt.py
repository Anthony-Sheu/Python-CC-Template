def kmp(txt, pat):
    m, n = len(pat), len(txt)
    lps, i, j, l, k = [0] * m, 0, 0, 0, 1
    while k < m:
        if pat[k] == pat[l]: l += 1; lps[k] = l; k += 1
        else:
            if l: l = lps[l - 1]
            else: lps[k] = 0; k += 1
    while i < n:
        if pat[j] == txt[i]: i += 1; j += 1
        if j == m: return i - j
        elif i < n and pat[j] != txt[i]:
            if j: j = lps[j - 1]
            else: i += 1
    return -1
