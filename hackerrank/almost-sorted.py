def asort(a):
    def candidate():
        e = []
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                e.append(i)
        if len(e) > 1:
            # one after another?
            one_after = True
            for i in range(len(e)-1):
                if e[i+1]-e[i] != 1:
                    one_after = False
                    break
            if one_after:
                # Reverse
                return ("reverse", e[0], e[-1]+1)
            if len(e) == 2:
                # Two mistakes
                return ("swap", e[0], e[-1]+1)
        else:
            return ("swap", e[0], e[0]+1)
        return None
    r = candidate()
    if not r:
        return "no"
    if r[1]>0:
        if a[r[1]-1]>a[r[2]]:
            return "no"
    if r[2]<len(a)-1:
        if a[r[1]]>a[r[2]+1]:
            return "no"
    return "yes\n%s %s %s" % (r[0], r[1]+1, r[2]+1)

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
print asort(a)
