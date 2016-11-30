max_found = 0
def number_needed(a, b):
    def calc_freq(arr):
        result = {}
        for ch in arr:
            result[ch] = result.get(ch, 0) + 1
        return result
    l = 0
    aa = calc_freq(a)
    bb = calc_freq(b)
    for ch in aa:
        l += min(aa.get(ch, 0), bb.get(ch, 0))
    return len(a) + len(b) - 2 * l

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
