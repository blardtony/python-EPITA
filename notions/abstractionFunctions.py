#La compréhension des abstractions fonctionnelles via leur domaine, leur gamme et leur intention est essentielle pour les utiliser correctement dans un programme complexe.


#les deux fonctions suivantes d'élévation au carré d'un nombre doivent être indiscernables. Chacune prend un argument numérique et produit le carré de ce nombre comme valeur.

def square(x):
    return mul(x, x)

def square(x):
    return mul(x, x-1) + x