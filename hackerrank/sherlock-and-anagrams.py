def anagrams(s):
    r = 0
    def freq(i, sz, other=None):
        fr = {}
        for idx in range(i, i+sz):
            ch = s[idx]
            if other and ch not in other:
                return None
            v = fr.get(ch, 0)+1
            fr[ch] = v
            if other and other.get(ch, 0)<v:
                return None
        return fr
    for sz in range(1, len(s)+1):
        fr = [freq(i, sz) for i in range(len(s)-sz+1)]
        for ib in range(len(s)-sz+1):
            fb = fr[ib]
            for ie in range(ib):
                fe = fr[ie]
                ok = False
                if len(fe) == len(fb):
                    ok = True
                    for ch in fb:
                        if ch not in fe or fb[ch] != fe[ch]:
                            ok = False
                            break
                if ok:
                    r += 1
    return r

n = int(raw_input().strip())
for i in range(n):
    s = raw_input().strip()
    print anagrams(s)
