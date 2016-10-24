def fibonacci(n):
    if n == 0:
        return 0,0
    elif n == 1:
        return 1,0
    else:
        n1,n2 = fibonacci(n-1)
        return n2+n1,n1
n = int(raw_input())
f,n1 = fibonacci(n)
print(f)
