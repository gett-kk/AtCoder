n, v = map(int, input().split())
w = list(map(int, input().split()))

ans = float("-inf")

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if (i + 1) + (j + 1) + (k + 1) <= v:
                ans = max(ans, w[i] + w[j] + w[k])

print(ans)
