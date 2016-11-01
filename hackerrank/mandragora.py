def max_points(a):
    n = 0
    for i in a:
        n += i
    mx = n    
    s = 0
    for i in range(len(a)-1):
        s += a[i]
        st = i+2
        pts = (n-s)*st
        if pts > mx:
            mx = pts
    return mx

q = int(raw_input().strip())
for i in range(q):
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    print max_points(sorted(a))
