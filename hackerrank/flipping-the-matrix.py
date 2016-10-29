def find_max(a, n):
    r = 0
    for j in range(n):
        jj = -1-j
        for i in range(n):
            ii = -1-i
            r += max(a[j][i], a[jj][ii], a[j][ii], a[jj][i])
    return r

q = int(raw_input().strip())
for i in range(q):
    n = int(raw_input().strip())
    a = []
    for j in range(2*n):
        a.append(map(int, raw_input().strip().split(' ')))
    print find_max(a, n)
