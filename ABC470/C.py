n, q = map(int, input().split())
a = [0] * n

nonzero = set()
xor = 0

for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1]

        xor ^= a[x - 1]
        a[x - 1] += 1
        xor ^= a[x - 1]

        nonzero.add(x - 1)

    elif query[0] == 2:
        remove = []

        for i in nonzero:
            xor ^= a[i]
            a[i] -= 1
            xor ^= a[i]

            if a[i] == 0:
                remove.append(i)

        for i in remove:
            nonzero.remove(i)   

    print(xor)
    