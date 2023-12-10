n = int(input())
scores_dataset = []
for i in range(n):
    d = {}
    d["Name"]=str(input())
    d["City"]=str(input())
    d["SeqNo"]=int(input())
    d["Mathematics"]=int(input())
    d["Physics"]=int(input())
    d["Chemistry"]=int(input())
    scores_dataset.append(d)
