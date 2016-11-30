def count_steps(s):
    r = 0
    for i in range(2, len(s)):
        if s[i-2] == '0' and s[i-1] == '1' and s[i] == '0':
            s[i] = '1'
            r += 1
    return r
n = int(raw_input().strip())
B = raw_input().strip()
print count_steps(list(B))
