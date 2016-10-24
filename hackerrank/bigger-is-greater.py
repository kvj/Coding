def bigger(data):
    s = list(data)
    for i in range(len(s)-2, -1, -1):
        if s[i]<s[i+1]:
            # in right tail find smallest bigger than s[i]
            maxr = i+1
            for j in range(i+1, len(data)):
                if s[j]<s[maxr] and s[j]>s[i]:
                    maxr = j
            return s[:i]+[s[maxr]]+sorted(s[i:maxr]+s[maxr+1:])
    return None
n = int(raw_input().strip())
for i in range(n):
    s = raw_input().strip()
    ss = bigger(s)
    print ''.join(ss) if ss else 'no answer'
