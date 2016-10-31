import math
def enc(s):
    sq = math.sqrt(len(s))
    m = int(math.floor(sq))
    n = int(math.ceil(sq))
    if m*n < len(s):
        m += 1
    ll = len(s)+n-1
    tail = len(s) % n
    if tail == 0:
        tail = n
    res = [' ' for i in range(ll)]
    for idx in range(len(s)):
        j = int(idx / n)
        i = idx % n
        pos = i*(m+1)+j
        if i>tail:
            pos -= i-tail
        res[pos] = s[idx]
    return ''.join(res)

s = raw_input().strip()
print enc(s.replace(' ', ''))
