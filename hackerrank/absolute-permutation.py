t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = map(int, raw_input().strip().split(' '))
    perm = []
    if k == 0:
        for i in range(n):
            perm.append(i+1)
    else:
        if n % 2 == 0 and n % k == 0:
            for i in range(n / k / 2):
                for j in range(k):
                    perm.append(k + 1 + j + 2*k*i)
                for j in range(k):
                    perm.append(1 + j + 2*k*i)
        else:
            perm = [-1]
    print ' '.join(map(str, perm))
