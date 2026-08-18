import os

folder_name = input()

generate_files = ["A.py", "B.py", "C.py", "D.py"]

try:
    os.makedirs(folder_name)
except FileExistsError:
    print(f"{folder_name}は既に存在しています。") 
    exit()

for file in generate_files:
    path = os.path.join(folder_name, file)
    with open(path, "x", encoding="utf-8"):
        pass
