from collections import defaultdict

n, q = map(int, input().split())

ranges = defaultdict(list)
for _ in range(q):
    l, r, x = map(int, input().split())
    ranges[x].append((l, r))

diff = [0] * (n + 2)

for _range in ranges.values():
    _range.sort()

    start, end = _range[0]
    for l, r in _range[1:]:
        if l <= end:
            end = max(end, r)
        else:
            diff[start] += 1
            diff[end + 1] -= 1
            start, end = l, r

    diff[start] += 1
    diff[end + 1] -= 1

ans = []
pref = 0
for i in range(1, n + 1):
    pref += diff[i]
    ans.append(pref)

print(*ans)
