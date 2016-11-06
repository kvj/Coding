def decode_xor(a, n, k):
    r = [0 for i in range(n)] # Result
    r[0] = a[0] # Not changed
    rx = a[0]
    if k >= n:
        # Can find all
        to = n
    else:
        to = k
    for i in range(1, to):
        r[i] = a[i-1] ^ a[i]
        rx = rx ^ r[i]
    for i in range(to, n):
        rx = rx ^ r[i - to]
        r[i] = rx ^ a[i]
        rx = rx ^ r[i]
    return r
    

n, k = map(int, raw_input().strip().split(' '))
arr = map(int, raw_input().strip())

print ''.join(map(str, decode_xor(arr, n, k)))
