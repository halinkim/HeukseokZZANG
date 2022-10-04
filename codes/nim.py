def mex(s):
    if not s:
        return 0
    for i in range(100):
        if i not in s:
            return i

b = list(multiinput())
dp = [0] * 501
for i in range(1, 501):
    s = set()
    for bb in b:
        if i - bb >= 0:
            s.add(dp[i - bb])
    dp[i] = mex(s)

for _ in range(5):
    x, y = multiinput()
    if (dp[x] ^ dp[y]) == 0:
        print('B')
    else:
        print('A')