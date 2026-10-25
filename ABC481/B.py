n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = sum(x == k for x in a)

for i in range(n - 1):
    if (a[i] < k < a[i + 1]) or (a[i + 1] < k < a[i]):
        ans += 1

print(ans)
