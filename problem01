a = int(input())
b = int(input())
al = []
bl = []
coprime = True 
for i in range(2,a+1):
    if a%i == 0:
        al.append(i)
for i in range(2,b+1):
    if b%i == 0:
        bl.append(i)
for i in al:
    for j in bl:
        if i == j:
            coprime = False

if coprime == True:
    print("Coprime")
else:
    print("Not Coprime")
