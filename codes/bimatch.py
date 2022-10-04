# N명의 직원이 M개의 일을 나누어서 할 때,
# i번째 직원이 할 수 있는 일이 정해져 있음
# 할 수 있는 최대 일의 개수 구하기
from collections import deque
adj = []
n, m = map(int, input().split())
for i in range(n):
    s = list(map(int, input().split()))[1:]
    ss = [0] * m
    for j in s:
        ss[j - 1] = 1
    adj.append(ss)

aMatch = [-1] * n
bMatch = [-1] * m

def dfs(a, visited):
    if visited[a]:
        return 0
    visited[a] = 1
    for b in range(0, m):
        if adj[a][b]:
            if bMatch[b] == -1 or dfs(bMatch[b], visited):
                aMatch[a] = b
                bMatch[b] = a
                return 1
    return 0
def bipartiteMatch():
    size = 0
    for start in range(0, n):
        visited = [0] * n
        if dfs(start, visited):
            size += 1
    return size