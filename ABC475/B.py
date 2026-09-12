n = int(input())
a = list(map(int, input().split()))

ans = [0] * 3

now = 0
for i in range(n):
    if a[i] % 1000 == 0:
        now = 0
    else:
        now = (a[i] // 1000 + 1) * 1000 - a[i]

    hundreds = now // 100
    now %= 100
    tens = now // 10
    now %= 10
    ones = now

    ans[0] += ones
    ans[1] += tens
    ans[2] += hundreds

print(*ans)
