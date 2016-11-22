def can_make(a, b):
    A = a.upper()
    ia = 0
    ib = 0
    while ib < len(b) or ia < len(a):
        # Search b[ib] in a from ia
        idx = -1
        for i in range(ia, len(a)):
            if (ib == len(b) and a[i] != A[i]) or (ib < len(b) and A[i] == b[ib]):
                # Found
                idx = i
                break
            if a[i] == A[i]:
                # We can't skip BIG - Let's Find last char in b
                for j in range(ib-1, -1, -1):
                    if b[j] == a[i]:
                        idx = i
                        ib = j
                        break
                if idx == -1: # Did not find
                    return False
                break
        if idx == -1:
            return False
        ib += 1 if ib < len(b) else 0
        ia = idx+1
    return True
            
n = int(raw_input().strip())
for i in range(n):
    a = raw_input().strip()
    b = raw_input().strip()
    print 'YES' if can_make(a, b) else 'NO'
