import math

def and_sum(a, b):
    if a == 0:
        return 0
    la = int(math.log(a, 2))
    lb = int(math.log(b, 2))
    if lb != la:
        return 0
    r = 0
    for p in range(la, 0, -1):
        ps = 1 << p
        if (ps & a) ^ (ps & b) == 0:
            # Both have
            r = r | (ps & a)
        else:
            return r
    return a

q = int(raw_input().strip())
for i in range(q):
    a, b = map(int, raw_input().strip().split(' '))
    print and_sum(a, b)
