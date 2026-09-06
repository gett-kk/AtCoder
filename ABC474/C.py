n, q = map(int, input().split())
p = list(map(int, input().split()))

a = []
for _ in range(q):
    a.append(int(input()))

seen = [False] * (n + 1)
moved = []

for x in reversed(a):
    if not seen[x]:
        moved.append(x)
        seen[x] = True

moved.reverse()

unmoved = []
for x in p:
    if not seen[x]:
        unmoved.append(x)

print(*(unmoved + moved))
