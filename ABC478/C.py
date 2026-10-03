n, k = map(int, input().split())
a = list(map(int, input().split()))

b = sorted(a)

diff = [i for i in range(n) if a[i] != b[i]]

if not diff or diff[-1] - diff[0] + 1 <= k:
    print("Yes")
else:
    print("No")
