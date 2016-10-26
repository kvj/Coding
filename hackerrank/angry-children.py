n = int(raw_input().strip())
k = int(raw_input().strip())
a = []
for i in range(n):
    a.append(int(raw_input().strip()))
a = sorted(a)
m = a[-1]-a[0]
for i in range(n-k+1):
    mm = a[i+k-1]-a[i]
    if mm < m:
        m = mm
print m
