def f(n):
    if n == 0:
        return 1
    else:
        return n*f(n-1)

def all_combinations(st1, st2, st3, k):
    n = 0
    d = 1
    # https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%B5%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0#.D0.9F.D0.B5.D1.80.D0.B5.D1.81.D1.82.D0.B0.D0.BD.D0.BE.D0.B2.D0.BA.D0.B8_.D1.81_.D0.BF.D0.BE.D0.B2.D1.82.D0.BE.D1.80.D0.B5.D0.BD.D0.B8.D0.B5.D0.BC
    for st in [st1, st2, st3]:
        n += st
        d *= f(st)
    return f(n)/d

def steps(n):
    found = 0
    for st1 in range(n+1):
        for st2 in range((n-st1)/2+1):
            dist = st1 + 2*st2
            if dist <= n and (n - dist) % 3 == 0:
                st3 = (n-dist) / 3
                found += all_combinations(st1, st2, st3, n)
    return found

s = int(raw_input().strip())
for a0 in xrange(s):
    n = int(raw_input().strip())
    total = steps(n)
    print total
