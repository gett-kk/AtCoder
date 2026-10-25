from collections import defaultdict

q = int(input())
d = defaultdict()
idx = 1

for query in range(q):
    s = input()

    if s not in d:
        d[s] = idx
        idx += 1

    print(d[s])
