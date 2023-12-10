def dict_to_list(D):
    L = []
    for key in D:
        L.append((key,D[key]))
    return L

def list_to_dict(L):
    D = dict()
    for l in L:
        D[l[0]] = l[1]
    return D
