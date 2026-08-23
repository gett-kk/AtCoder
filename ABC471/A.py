a, b = map(int, input().split())

if a + b == 9 or a - b == 9 or a * b == 9 or a / b == 9:
    print("Nine")
else:
    print("Nein")
