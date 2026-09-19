import bisect

n, m, k = map(int, input().split())
x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

pref_a = [0] * (n + 1)
for i in range(n):
    pref_a[i + 1] = pref_a[i] + a[i]

pref_b = [0] * (m + 1)
for j in range(m):
    pref_b[j + 1] = pref_b[j] + b[j]

need_k = [0] * (m + 1)
for j in range(m):
    need_k[j + 1] = need_k[j] + (b[j] + k - 1) // k

ans = 0
for cnt_b in range(m + 1):
    used = need_k[cnt_b]
    if used > y:
        break

    rem_k = y - used
    sum_b = pref_b[cnt_b]
    change = used * k - sum_b
    total = x + change + rem_k * k

    cnt_a = bisect.bisect_right(pref_a, total) - 1

    ans = max(ans, cnt_b + cnt_a)

print(ans)
