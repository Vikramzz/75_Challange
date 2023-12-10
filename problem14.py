def factors(n):
    s = set()
    for i in range(1,n+1):
        if n%i == 0:
             s.update([i])
    return s

def common_factors(a, b):
    S1 = factors(a)
    S2 = factors(b)
    return S1.intersection(S2)

def factors_upto(n):
    d = dict()
    for i in range(1,n+1):
       d[i] = factors(i)
    return d
