num = str(input())
valid = True
if len(num)!=10:
    valid = False
if num[0]=="0":
    valid = False
if num[0]=="1":
    valid = False
if num[0]=="2":
    valid = False
if num[0]=="3":
    valid = False
if num[0]=="4":
    valid = False
if num[0]=="5":
    valid = False
for i in num :
    count = 0
    frq = 0
    for j in num:
        if i == j:
            count +=1
            frq += 1
        else:
            frq =0
    if count > 7 or frq > 5:
        valid = False
if valid:
    print("valid")
else:
  print("Not Valid")
