n, s, l = map(int, input().split())
a = list(map(int, input().split()))

s -= 1
ans = 0

prefix = [0] * n
for i in range(n - 1):
    prefix[i + 1] = prefix[i] + a[i]

for left in range(s + 1):
    for right in range(s, n):
        x = prefix[s] - prefix[left]
        y = prefix[right] - prefix[s]
        if min(2 * x + y, x + 2 * y) <= l:
            ans = max(ans, right - left + 1)

print(ans)
