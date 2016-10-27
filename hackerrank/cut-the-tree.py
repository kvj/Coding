def find_min_(a, s):
    tasks = [0]
    idx = 0
    while idx < len(tasks):
        t = tasks[idx]
        edges = []
        for i in a[t][1]:
            if i != a[t][2]:
                a[i][2] = t # Set parent
                edges.append(i)
        a[t][1] = edges
        tasks.extend(edges)
        idx += 1
    mind = s
    idx = len(tasks)-1
    while idx>0:
        t = tasks[idx]
        ss = a[t][0]
        for i in a[t][1]:
            ss += a[i][3]
        d = abs(s - 2 * ss)
        if d < mind:
            mind = d
        a[t][3] = ss
        idx -= 1
    return mind

n = int(raw_input().strip())
a = []
s = 0
for i in map(int, raw_input().strip().split(' ')):
    a.append([i, [], -1, 0])
    s += i # Sum
for i in range(n-1):
    e1, e2 = map(int, raw_input().strip().split(' '))
    a[e1-1][1].append(e2-1)
    a[e2-1][1].append(e1-1)
print find_min_(a, s)
