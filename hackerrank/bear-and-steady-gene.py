def fix(s, chars):
    n = len(s) / len(chars)
    mx = len(s)
    fi = {}
    for i in range(len(chars)):
        fi[chars[i]] = 0
    i = 0
    j = -1
    while i < len(s):
        fi[s[i]] += 1 # Collect freq for the left side
        if fi[s[i]] > n: # Full
            while i>=0: # Step back
                fi[s[i]] -= 1
                i -= 1
                while -j<=len(s): # Fill freq for the right side
                    if fi[s[j]] == n:
                        m = len(s) - i + j
                        if m < mx:
                            mx = m
                        break
                    fi[s[j]] += 1                        
                    j -= 1
            break
        i += 1
    if i == len(s): # No replacement needed
        return 0
    return mx

n = int(raw_input().strip())
s = raw_input().strip()
print fix(s, 'ACTG')
