import sys

# sys.setrecursionlimit(10**6)
# import decimal

# import math
# from collections import deque
# import itertools
# from collections import Counter
# from queue import PriorityQueue
# import heapq
# import decimal
# import random
# from bisect import bisect_left, bisect_right
# import fractions

# import re
# import datetime

input = sys.stdin.readline


def multiinput():
    return map(int, input().split())

class LazyFenwick:
    def __init__(self, size):
        self.size = size
        self.bit = [[0] * (size + 1) for _ in range(2)]

    def update(self, bitType, idx, diff):
        while idx <= self.size:
            self.bit[bitType][idx] += diff
            idx += idx & -idx

    def rangeUpdate(self, a, b, diff):
        self.update(0, a, diff)
        self.update(0, b + 1, -diff)
        self.update(1, a, diff * (a - 1))
        self.update(1, b + 1, -diff * b)

    def getBitValue(self, bitType, idx):
        ans = 0
        while idx > 0:
            ans += self.bit[bitType][idx]
            idx -= idx & -idx
        return ans

    def prefixSum(self, idx):
        return self.getBitValue(0, idx) * idx - self.getBitValue(1, idx)

    def query(self, a, b):
        return self.prefixSum(b) - self.prefixSum(a - 1)



# decimal.getcontext().prec = 1111

def main(tc):
    n, m, k = multiinput()
    s = LazyFenwick(n)
    for _ in range(1, n + 1):
        i = int(input())
        s.rangeUpdate(_, _, i)
    for _ in range(m + k):
        a, *q = multiinput()
        if a == 1:
            b, c, d = q
            s.rangeUpdate(b, c, d)
        else:
            b, c = q
            print(s.query(b, c))




# for tc in range(int(input())):
for tc in range(1):
    main(tc)
