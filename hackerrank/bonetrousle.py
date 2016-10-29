def find_boxes(n, k, b):
    # n boxes total, sum is k, b boxes needed 
    bb = [0 for i in range(b)]
    # Make start position
    bmin = 0 # min number of sticks
    bmax = 0
    for i in range(b):
        bmax += n - i - 1
        bmin += i
        bb[i] = i
    if bmin > k:
        return None
    if bmax < k:
        return None
    up = int((k - bmin) / b)
    if up > 0:
        for i in range(b):
            bb[i] += up
    for i in range((k - bmin) % b):
        bb[b - i - 1] += 1
    return bb

q = int(raw_input().strip())
for i in range(q):
    k, n, b = map(int, raw_input().strip().split(' '))
    r = find_boxes(n, k-b, b)
    print ' '.join(map(lambda x: str(x+1), r)) if r else -1
