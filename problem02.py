import sys 
str = str(input())
T = 0
for i in str:
    if i == ".":
        print("Float")
        sys.exit()
for i in str:
    if i in  "123456789":
        T +=1
if T == len(str):
    print("Integer")
else:
    print("None")
