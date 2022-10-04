INF = 10**9
# V = 10
# capacity = [[1] * V for _ in range(V)]
# flow = [[0] * V for _ in range(V)]


V = 4
capacity = [[0, 1, 3, 0], [0, 0, 1, 2], [0, 0, 0, 1], [0, 0, 0, 0]]
flow = [[0, 0, 0, 0] for _ in range(4)]


def networkFlow(source, sink):
    totalFlow = 0
    while 1:
        parent = [-1] * V
        q = deque()
        parent[source] = source
        q.append(source)
        while q and parent[sink] == -1:
            here = q.popleft()
            for there in range(0, V):
                if capacity[here][there] - flow[here][there] > 0 and parent[there] == -1:
                    q.append(there)
                    parent[there] = here
        if parent[sink] == -1:
            break
        amount = INF
        p = sink
        while p != source:
            amount = min(capacity[parent[p]][p] - flow[parent[p]][p], amount)
            p = parent[p]
        p = sink
        while p != source:
            flow[parent[p]][p] += amount
            flow[p][parent[p]] -= amount
            p = parent[p]
        totalFlow += amount
    return totalFlow