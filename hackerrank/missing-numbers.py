def freq(a):
    fr = {}
    for v in a:
        fr[v] = fr.get(v, 0) + 1
    return fr
n1 = int(raw_input().strip())
a1 = map(int, raw_input().strip().split(' '))
n2 = int(raw_input().strip())
a2 = map(int, raw_input().strip().split(' '))
fr = {}
for v in a1:
    fr[v] = fr.get(v, 0) + 1
missing = []
for v in a2:
    vv = fr.get(v, 0) - 1
    if vv == -1:
        missing.append(v)
    fr[v] = vv
print ' '.join(map(str, sorted(missing)))
