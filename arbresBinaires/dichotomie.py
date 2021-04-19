def dichotomie(t, v):
    a = 0
    b = len(t) - 1
    while a <= b:
        m = (a + b) // 2
        if t[m] == v:
            # on a trouvé v
            return "Le nombre " + str(v) + " est dans cette liste à l'index " + str(m)
        elif t[m] < v:
            a = m + 1
        else:
            b = m - 1
    # on a a > b
    return "Le nombre " + str(v) + " n'est pas dans cette liste"

tab = [3,4,9,15,16,21,25,30,33,38,43,44]

print(dichotomie(tab, 38))
print(dichotomie(tab, 8))

#Algo plus rapide 

def dicho2(t, v):
    a = 0
    b = len(t)
    if b == 0:
        # il faut traîter le cas
        # où la liste est vide
        return False
    while b > a + 1:
        m = (a + b) // 2
        if t[m] > v:
            b = m
        else:
            a = m
    return t[a] == v