def lonely_integer(a):
    r = a[0]
    for i in range(1, len(a)):
        r = r ^ a[i]
    return r

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)
