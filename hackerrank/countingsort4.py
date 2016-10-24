n = int(raw_input().strip())
a = []
n2 = n/2
maxi = 0
for i in range(n):
    l = raw_input().strip().split(' ')
    li = int(l[0])
    a.append((i, li, l[1] if i >= n2 else '-'))
    if li > maxi:
        maxi = li
idx = [[0, 0] for i in range(maxi+1)]
for item in a:
    idx[item[1]][0] += 1
lidx = 0
for i in range(len(idx)):
    v = idx[i][0]
    idx[i][0] = lidx
    lidx += v
res = ['' for i in range(n)]
for item in a:
    i = idx[item[1]]
    res[i[0]+i[1]] = item[2]
    i[1] += 1
print ' '.join(res)
