import heapq

q, v = map(int, input().split())

hq = []

for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        t, w = query[1], query[2]
        heapq.heappush(hq, t - w)

    elif query[0] == 2:
        t = query[1]
        
        if not hq:
            print(-1)
        else:
            val = heapq.heappop(hq)
            
            cur = min(v, -val + t)
            print(cur)