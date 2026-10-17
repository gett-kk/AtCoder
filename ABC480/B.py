from collections import defaultdict

n, m = map(int, input().strip().split())

d = {}
mp = defaultdict(set)

for i in range(n):
    s = input().strip()
    d[s] = i
    for j in range(len(s)):
        temp = s[:j] + "*" + s[j + 1 :]
        mp[temp].add(i)

ans = [0] * n

for _ in range(m):
    t = input().strip()

    if t in d:
        ans[d[t]] += 1
        continue

    temp = set()
    for j in range(len(t)):
        key = t[:j] + "*" + t[j + 1 :]
        temp.update(mp[key])
        if len(temp) > 1:
            break

    if len(temp) == 1:
        ans[temp.pop()] += 1

for x in ans:
    print(x)
