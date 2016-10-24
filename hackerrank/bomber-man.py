r,c,n = map(int, raw_input().strip().split(' '))
if n > 5:
    n = ((n-1) % 4)+5
f = []
for j in range(r):
    f.append(map(lambda ch: -1 if ch == '.' else 0, raw_input().strip()))
s = 1
b = 0 # Bomb number
if n % 2 == 0:
    for j in range(r):
        print ''.join(map(lambda x: 'O', range(c)))
else:
    while s < n:
        for j in range(r):
            for i in range(c):
                bombs = 0
                for idx in range(max(0, j-1), min(j+2, r)):
                    bombs += 1 if f[idx][i] == b else 0
                for idx in range(max(0, i-1), min(i+2, c)):
                    bombs += 1 if f[j][idx] == b else 0
                if bombs == 0:
                    f[j][i] = b+2
        s += 2
        b += 2
    for j in range(r):
        print ''.join(map(lambda i: 'O' if f[j][i] == b else '.', range(c)))
