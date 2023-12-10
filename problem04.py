n = int(input())
fact = []
for i in range(2,n+1):
    if n%i == 0:
        fact.append(i)
for i in fact:
    prime = True
    for j in range(2,i):
        if i%j == 0:
            prime = False
            break
    if prime == True:
        print(i)
