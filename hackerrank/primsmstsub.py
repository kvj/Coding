def find_weight(arr, s, n):
    marks = [False for i in range(n)]
    ml = 1
    marks[s] = True
    r = 0
    while ml < n:
        m = None
        for w in arr:
            if marks[w[0]] and not marks[w[1]] and (not m or w[2] < m[0]):
                m = [w[2], w[1]]
            if marks[w[1]] and not marks[w[0]] and (not m or w[2] < m[0]):
                m = [w[2], w[0]]
        r += m[0]
        marks[m[1]] = True
        ml += 1
    return r

n, m = map(int, raw_input().strip().split(' '))
arr = [None for i in range(m)]
for i in range(m):
    a, b, w = map(int, raw_input().strip().split(' '))
    arr[i] = [a-1, b-1, w]
s = int(raw_input().strip())-1
print find_weight(arr, s, n)
