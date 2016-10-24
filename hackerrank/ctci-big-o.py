import math
primes = [2]
def is_prime(v):
    if v == 1:
        return False
    i = 0
    while True:
        p = primes[i]
        if v == p:
            return True
        if p > math.sqrt(v):
            return True
        if v % p == 0:
            return False
        i += 1
        if i == len(primes):
            next_prime()
    return True
def next_prime():
    v = primes[-1]+1
    while True:
        if is_prime(v):
            primes.append(v)
            return v
        v += 1
p = int(raw_input().strip())
for _ in xrange(p):
    n = int(raw_input().strip())
    print 'Prime' if is_prime(n) else 'Not prime'
