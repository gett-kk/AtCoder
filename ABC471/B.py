from collections import defaultdict

n = int(input())
d = defaultdict(int)

for _ in range(n):
    s = input().lower()

    d[s] += 1

print(max(d.values()))