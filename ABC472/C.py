n, m, k = map(int, input().split())
a = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(1, n + 1):
    left = max(0, i - m)
    cal = prefix[i - 1] - prefix[left]

    if cal + a[i - 1] <= k:
        prefix[i] = prefix[i - 1] + a[i - 1]
        print("Yes")
    else:
        prefix[i] = prefix[i - 1]
        print("No")
