def min_diff(a):
    mn = -1
    mx = -1
    # Find min and max
    for i in range(len(a)):
        if mn == -1 or a[i] < a[mn]:
            mn = i
        if mx == -1 or a[i] > a[mx]:
            mx = i
    mn2 = -1
    mx2 = -1
    # Find min and max closest to found min and max before 
    for i in range(len(a)):
        if i != mn and a[i] >= a[mn] and (mn2 == -1 or a[i] < a[mn2]):
            mn2 = i
        if i != mx and a[i] <= a[mx] and (mx2 == -1 or a[i] > a[mx2]):
            mx2 = i
    if a[mn2] - a[mn] > a[mx] - a[mx2]:
        return a[mx] - a[mn2]
    else:
        return a[mx2] - a[mn]

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print min_diff(a)
