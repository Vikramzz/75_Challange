sentence = str(input()).split(" ")
d = dict()
for word in sentence:
    if word[0] in d :
        d[word[0]].append(word)
    else:
        d[word[0]] = [word]
print(d)
