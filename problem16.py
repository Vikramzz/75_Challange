sentense = str(input()).split(",")  
d = {}
for word in sentense:
    if word in d:
        d[word]+=1
    else:
        d[word] = 1
print(d)

d1 = {}
for i in range(len(sentense)):
    for word in d:
        if i == d[word]:
            if i in d1:
                d1[i].append(word)
            else:
                d1[i] = [word]
print(d1)
