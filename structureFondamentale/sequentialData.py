#chaînes de caractères (str),  tuples (tuples) et intervalles (range) sont des structures de données séquentielles

s = "timoleon" #Chaînes 
t = (1, 2, 3) #Tuples
r = range(1,10,2) #Range avec pour valeurs : 1 3 5 7 9

print(len(s),len(t),len(r))

print(
    s[0],
    s[len(s) - 1],
    t[0],
    t[len(t) - 1],
    r[0],
    r[len(r) - 1]
)

print(
    't' in s,
    'u' in s,
    2 in t,
    4 in t,
    1 in r,
    2 in r
)

for c in s:
    print(c)

for c in t:
    print(c)

for c in r:
    print(c)




#Listes

#On voit qu’en mémoire coexistent deux listes identiques en longueur et en contenu mais différentes en localisation
l1 = list('timoleon')
l2 = list(l1)

l3 = [3, 1, 4] + [1, 5, 9, 2] # Affiche [3, 1, 4, 1, 5, 9, 2]

l4 = [k**2 for k in range(10)] # Affiche [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

l5 = [(x, y) for x in range(3) for y in range(3)] # Affiche [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]


l1 == l2 # True

l2 is l1 # False Pas au même endroit en mémoire mais même valeurs

l3 = l1

l3 is l1 # True

for x in ['a', 'b', 'c']:
    print(x)

l1[3] = 'o' # Changement de la valuer à l'index 3

print(l1.index('t'))
print(l1.count('t'))

l1.append('m') # ajout la valeur m

l5 = [1,2,3]
l5.reverse() # Renverse l'ordre d'une liste
print(l5)

l5.sort()#Classe par ordre croissant dans une liste
print(l5)

print("Timoleon est un homme\npolitique\tgrec".split()) # split sans paramètre liste de chaînes obtenues en supprimant tous les caractères d’espacement 




