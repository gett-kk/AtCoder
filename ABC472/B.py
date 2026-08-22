n = int(input())
l = list(map(int, input().split()))

ans = float('inf')
all = sum(l)
right = 0
left = 0

for i in range(n):
    right += l[i]
    left = all - right
    ans = min(ans, abs(right - left))

print(ans)
