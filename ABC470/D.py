n, q = map(int, input().split())
p = list(map(lambda x: int(x) - 1, input().split()))  # 0-indexed

# p'
pd = [0] * n
for i in range(n):
    pd[p[i]] = i

is_inverted = False

for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x, y = query[1] - 1, query[2] - 1

        if not is_inverted:
            u, v = p[x], p[y]
            p[x], p[y] = v, u
            pd[u], pd[v] = y, x
        else:
            u, v = pd[x], pd[y]
            pd[x], pd[y] = v, u
            p[u], p[v] = y, x

    elif query[0] == 2:
        is_inverted = not is_inverted

ans = pd if is_inverted else p
print(*(i + 1 for i in ans))
