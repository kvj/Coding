def find_towers(a, k):
    tt = 0
    t = []
    for i in range(len(a)):
        if a[i] == 1:
            t.append(i)
    i = 0
    ti = 0
    t_on = 0
    while i < len(a):
        pos = i + k - 1
        tpos = -1
        while True:
            if ti >= len(t):
                break
            if t[ti] <= pos:
                tpos = t[ti]
                ti += 1
            else:
                break
        if tpos == -1:
            return -1
        i = tpos + k
        t_on += 1
    return t_on
n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
print find_towers(a, k)
