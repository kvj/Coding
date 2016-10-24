n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

def qs(s, l):
    if l - s < 2:
        return
    last = a[l-1]
    midx = s
    for i in range(s, l-1):
        if a[i] < last:
            # Swap
            v = a[i]
            a[i] = a[midx]
            a[midx] = v
            midx += 1
    v = a[l-1] # Swap last
    a[l-1] = a[midx]
    a[midx] = v
    print ' '.join(map(str, a))
    qs(s, midx)
    qs(midx+1, l)
qs(0, n)
