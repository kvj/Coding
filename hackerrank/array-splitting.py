def max_moves(a):    
    n = 0
    for i in a:
        n += i
    q = [[0, 0, len(a), n]]
    qidx = 0
    ml = 0
    while qidx < len(q):
        level, s, l, n = q[qidx]
        qidx += 1
        if l-s <= 1 or n % 2 != 0:
            if level > ml:
                ml = level
            continue
        n2 = n / 2
        nl = 0
        for i in range(s, l):
            nl += a[i]
            if nl == n2:
                # Found
                q.append([level+1, s, i+1, n2])
                q.append([level+1, i+1, l, n2])
                break
    return level        

q = int(raw_input().strip())

for i in range(q):
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    print max_moves(a)
