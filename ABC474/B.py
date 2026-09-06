n = int(input())
p = list(map(int, input().split()))

flag = True
for i in range(n):
    if (p[i] - 1) // 10 != i // 10:
        flag = False
        break

if flag:
    print("Yes")

else:
    print("No")
