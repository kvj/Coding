import math

def make_pal(num, n, k):
    nm = num[:] # Copy
    m = [-1 for i in range(n/2)]
    mc = 0 # Mistakes count
    n2 = int(math.ceil(float(n)/2))
    for i in range(n2):
        if num[i] != num[-1-i]:
            m[mc] = i
            mc += 1
    if mc > k:
        return -1 # Too many mistakes
    for i in range(mc):
        # Fix all mistakes, choose bigger
        ch = max(num[m[i]], num[-1-m[i]])
        nm[m[i]] = nm[-1-m[i]] = ch
    # Still have some - replace with 9
    l = k - mc # Number of changes left
    for i in range(n/2):
        ll = 0
        if nm[i] != '9' and nm[i] == num[i]:
            # Not 9 and not changed before
            ll += 1
        if nm[-1-i] != '9' and nm[-1-i] == num[-1-i]:
            # Not 9 and not changed before
            ll += 1
        if ll<=l:
            # Have enough
            l -= ll
            nm[i] = nm[-1-i] = '9'
        else:
            break # No more changes
    if l>0 and n % 2 == 1:
        nm[n/2] = '9'
    return ''.join(nm)

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
number = raw_input().strip()
print make_pal(list(number), n, k)
