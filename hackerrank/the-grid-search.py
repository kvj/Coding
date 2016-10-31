def read_matrix():
    m, n = map(int, raw_input().strip().split(' '))
    a = []
    for j in range(m):
        a.append(raw_input().strip())
    return a

def find_pattern(a, b):
    n = len(b[0])
    for j in range(len(a) - len(b) + 1):
        la = a[j]
        for i in range(len(la) - n + 1):
            ok = True
            for jj in range(len(b)):
                for ii in range(n):
                    if a[j+jj][i+ii] != b[jj][ii]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                return True
    return False

q = int(raw_input().strip())
for i in range(q):
    a = read_matrix()
    b = read_matrix()
    print 'YES' if find_pattern(a, b) else 'NO'
