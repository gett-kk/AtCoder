from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)

for i in range(n):
    d[a[i]] += 1

ans = 0
for key, value in d.items():
    if value % 2 != 0:
        ans += key

print(ans)
