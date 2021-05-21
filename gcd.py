def gcd(a,b):
    d = 0
    while ~a & 1 and ~b & 1: # if a and b are even:
        a = a // 2
        b = b // 2
        d = d + 1
    while a != b:
        if ~a & 1: # if a is even
            a = a//2
        elif ~b & 1: #elif b is even
            b = b//2
        else:
            b = (b - a)//2
    g = a
    return a * 2**d
