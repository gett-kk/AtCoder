s1 = input().strip()
s2 = input().strip()
flag = False

if s1[0] == "A":
    if s1[1] == "D" or s2[0] == "D":
        flag = True

if s1[1] == "A":
    if s1[0] == "D" or s2[1] == "D":
        flag = True

if s2[0] == "A":
    if s2[1] == "D" or s1[0] == "D":
        flag = True

if s2[1] == "A":
    if s2[0] == "D" or s1[1] == "D":
        flag = True

if flag:
    print("Yes")
else:
    print("No")
