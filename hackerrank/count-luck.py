def find_waves(a, n, m, si, sj, fi, fj):
    def has_choice(x, y):
        paths = ((x-1, y), (x+1, y), (x, y-1), (x, y+1))
        for xx, yy in paths:
            if xx>=0 and xx<n and yy>=0 and yy<m and a[yy][xx] in (0, 1):
                return True
        return False
    def step(x, y):
        a[y][x] = 1 # Was there
        if x == fi and y == fj:
            return True
        paths = ((x-1, y), (x+1, y), (x, y-1), (x, y+1))
        for xx, yy in paths:
            if xx>=0 and xx<n and yy>=0 and yy<m and a[yy][xx] == 0:
                if step(xx, yy):
                    a[yy][xx] = 2
                    return True
        return False
    step(si, sj)
    a[sj][si] = 2 # Start point
    k = 0
    for j in range(m):
        for i in range(n):
            if i == fi and j == fj:
                continue # Ignore last point
            if a[j][i] == 2 and has_choice(i, j):
                k += 1
    return k

nn = int(raw_input().strip())
for i in range(nn):
    si, sj = 0, 0
    fi, fj = 0, 0
    m,n = map(int, raw_input().strip().split(' '))
    a = []
    for j in range(m):
        l = []
        line = raw_input().strip()
        for i in range(n):
            ch = line[i]
            v = 0
            if ch == '*':
                fi, fj = i, j
            elif ch == 'M':
                si, sj = i, j
            elif ch == 'X':
                v = -1
            l.append(v)
        a.append(l)
    k = int(raw_input().strip())
    print 'Impressed' if k == find_waves(a, n, m, si, sj, fi, fj) else 'Oops!'
