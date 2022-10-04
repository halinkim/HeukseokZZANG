def moduloinv(p, q):
    mod = 1000000007
    expo = mod - 2
    while (expo):
        if (expo & 1):
            p = (p * q) % mod
        q = (q * q) % mod
        expo >>= 1

    return p