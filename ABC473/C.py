n, k = map(int, input().split())
a = list(map(int, input().split()))

classroom = [0] * (k + 1)
for i in range(n):
    classroom[a[i]] += 1

max_num = max(classroom)

ans = 0
for i in range(1, k + 1):
    if classroom[i] in (max_num, max_num - 1):
        ans += 1

print(ans)
