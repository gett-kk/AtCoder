n = int(input())
a = list(map(int, input().split()))

top = sorted(a[0:3], reverse=True)
print(top[2])

for i in range(3, n):
    if a[i] < top[2]:
        pass
    elif a[i] < top[1]:
        top[2] = a[i]
    elif a[i] < top[0]:
        top[2] = top[1]
        top[1] = a[i]
    else:
        top[2] = top[1]
        top[1] = top[0]
        top[0] = a[i]

    print(top[2])
