n,m = map(int, raw_input().strip().split(' '))
a = []
for i in range(n):
    a.append([])
for i in range(m):
    u,v = map(int, raw_input().strip().split(' '))
    a[v-1].append(u-1)
trees = 0
def walk(i):
    global trees
    # Return number of edges removed
    s = 1
    for j in a[i]:
        ss = walk(j)
        if ss % 2 == 0:
            # print 'Found tree at:', i, j
            trees += 1
        else:
            s += ss
    return s
walk(0)
print trees
