n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

valid_stone = set()

for i in range(n):
    if a[i] > b[i]:
        valid_stone.add(i + 1)

if len(valid_stone) == 0:
    print("No")
    exit()

print("Yes")

ans = [10**18 if (i + 1) in valid_stone else 1 for i in range(n)]
print(*ans)
