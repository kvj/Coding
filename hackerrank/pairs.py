def pairs(a, k):
    i = 0
    j = 1
    r = 0
    while i < len(a):
        while j < len(a) and a[j] - a[i] <= k:
            if a[j] - a[i] == k:
                r += 1
            j += 1
        if j == len(a):
            break
        while i < len(a) and a[j] - a[i] > k:
            i += 1
    return r

n, k = map(int, raw_input().strip().split(' '))
a = sorted(map(int, raw_input().strip().split(' ')))
print pairs(a, k)
