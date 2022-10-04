# a, b의 gcd가 1일 때만 작동
# ax + by = 1의 해를 리턴
def eea(a, b):
    s0, s1, t0, t1 = 1, 0, 0, 1
    r0, r1 = a, b
    q1 = r0 // r1
    while 1:
        s0, s1, t0, t1 = s1, s0 - s1 * q1, t1, t0 - t1 * q1
        r0, r1 = r1, r0 - r1 * q1
        if r1:
            q1 = r0 // r1
        else:
            return s0, t0