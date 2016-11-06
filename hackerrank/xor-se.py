def gen_next(s, i, j, x):
    p = s
    r = 0
    idx = i + 1
    zeroes = 0
    while idx < j+1:
        p = p ^ idx
        if x and x(p, idx):
            r = r ^ p
        if p == 0:
            zeroes += 1
            if zeroes == 1:
                skip = int((j - idx) / 8)
                idx += 8 * skip
        idx += 1
    return r

def find_sum(L, R):
    s = L
    if L > 3:
        s = L - (L % 4) - 1
    else:
        s = 0
    def handler(x, i):
        return True if i >= L else False
    r = gen_next(0, s, R, handler)
    return r

Q = int(raw_input().strip())
for a0 in xrange(Q):
    L,R = raw_input().strip().split(' ')
    L,R = [long(L),long(R)]
    print find_sum(L, R)
