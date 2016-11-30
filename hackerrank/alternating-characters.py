def num_removes(s):
    r = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            r += 1
    return r

t = int(raw_input().strip())
for i in range(t):
    s = raw_input().strip()
    print num_removes(s)
