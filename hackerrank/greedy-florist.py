n, k = map(int, raw_input().strip().split(' '))
a = sorted(map(int, raw_input().strip().split(' ')), reverse=True)
r = 0
for i in range(n): # Buy n flowers
    inc = int(i / k) # Price increase
    r += (inc+1)*a[i]
print r
