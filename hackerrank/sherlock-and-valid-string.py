def can_do(s):
    f = {} # Frequences
    fn = {} # Number of chars of that number
    fm = 0
    u = 0
    for i in range(len(s)):
        ch = s[i]
        n = f.get(ch, 0)
        if n > 0:
            fn[n] -= 1
        if n == 0:
            u += 1
        n += 1
        fn[n] = fn.get(n, 0) + 1
        f[ch] = n
        if n > fm:
            # New maximum
            fm = n
        def check_tail(fm, u):
            others = i+1
            needed = u*fm
            return needed - others
        if check_tail(fm, u) <= len(s) - i: # Make zero or one removal in future
            continue
        if fn[fm] == 1 and check_tail(fm-1, u) <= len(s) - i - 1: # Remove one of biggest
            continue
        if fn.get(1) == 1 and check_tail(fm, u-1) <= len(s) - i - 1: # Remove only one char
            continue
        return False
    return True

s = raw_input().strip()
print 'YES' if can_do(s) else 'NO'
