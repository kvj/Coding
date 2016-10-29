def find_bribes(a):
    brt = 0
    for i in range(len(a)):
        idx = len(a) - 1 - i
        if idx > 1 and a[idx-2] == idx:
            # Two steps away
            a[idx-2] = a[idx-1]
            a[idx-1] = a[idx]
            a[idx] = idx
            brt += 2
        elif idx > 0 and a[idx-1] == idx:
            # One step away
            a[idx-1] = a[idx]
            a[idx] = idx
            brt += 1
        elif a[idx] != idx:
            return -1
    return brt

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    q = map(lambda x: int(x) - 1, raw_input().strip().split(' '))
    br = find_bribes(q)
    print br if br >= 0 else 'Too chaotic'
