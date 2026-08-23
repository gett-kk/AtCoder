import bisect

n = int(input())
a = list(map(int, input().split()))

a.sort()

idx = bisect.bisect_left(a, 0)
left = a[:idx]
right = a[idx:][::-1]

cur = ans = 0

for _ in range(n):
    if not right or (left and abs(cur - left[-1]) <= abs(cur - right[-1])):
        next = left.pop()
    else:
        next = right.pop()
        
    ans += abs(cur - next)
    cur = next

print(ans)