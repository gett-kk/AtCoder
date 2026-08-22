s = list(input())

for i in range(len(s)):
    if s[i] != "A":
        s[i] = "."

print("".join(s))
