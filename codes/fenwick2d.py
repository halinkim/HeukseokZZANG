class Fenwick2D:
    def __init__(self, w, h):
        self.data = [[0] * h for _ in range(w)]
        self.w = w
        self.h = h
    def prefix_sum(self, r, c):
        cnt = 0
        while r > 0:
            cc = c
            while cc > 0:
                cnt += self.data[r][cc]
                cc -= cc & -cc
            r -= r & -r
        return cnt
    def add(self, r, c, diff):
        while r <= self.w:
            cc = c
            while cc <= self.h:
                self.data[r][cc] += diff
                cc += cc & -cc
            r += r & -r