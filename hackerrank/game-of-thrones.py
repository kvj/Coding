string = raw_input().strip()
 
found = True

f = {} # Freq
for s in string:
    f[s] = f.get(s, 0) + 1
odds = 0
for s in f:
    if f[s] % 2 == 1:
        odds += 1
        if odds > 1:
            found = False
            break

if not found:
    print("NO")
else:
    print("YES")
