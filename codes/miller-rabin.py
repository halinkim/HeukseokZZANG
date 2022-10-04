def power(x, y, p):
    res = 1

    while y > 0:
        if y % 2 != 0:
            res = (res * x) % p
        y //= 2
        x = (x * x) % p
    return res
def miller_rabin(n, a):
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d = d // 2

    x = power(a, d, n)
    if x == 1 or x == n - 1:
        return True

    for i in range(r - 1):
        x = power(x, 2, n)
        if x == n - 1:
            return True
    return False