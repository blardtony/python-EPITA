#Adressage direct

def valeur(c, t):
    """renvoie la valeur correspondante à la clé c dans le dictionnaire t"""
    return t[c] 

def inserer(c, v, t):
    """insere le couple clé/valeur c -> v dans le dictionnaire t"""
    t[c] = v

def supprimer(c, t):
    """supprime l'association de clé c du dictionnaire t"""
    t[c] = None