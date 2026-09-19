import sys

n = int(input())
s = input()
t = input()

for i in range(n):
    if t[i] == "*" or s[i] == t[i]:
        continue
    else:
        print("No")
        sys.exit()

print("Yes")
