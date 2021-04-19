#Exemple
class Noeud:
   def __init__(self, valeur, gauche=None, droite=None):
      self.valeur = valeur
      self.gauche = gauche
      self.droite = droite

a = Noeud(3, Noeud(83, droite=Noeud(56, gauche=Noeud(49, Noeud(41), Noeud(89, droite=Noeud(57, Noeud(28), Noeud(31, droite=Noeud(58, gauche=Noeud(45)))))))), Noeud(32))

def insertion_ABR(x, a):
    """
    Insère la nouvelle valeur x dans l'ABR dont la racine est a.
    """

    if a is None:
        return Noeud(x)
    else:
        v = a.valeur

        if x < v:
            # On insère x dans le sous-arbre à gauche
            nouveau_gauche = insertion_ABR(x, a.gauche)
            return Noeud(v, 
                         gauche=nouveau_gauche, 
                         droite=a.droite)
        else:
            # On insère x dans le sous-arbre à droite
            nouveau_droite = insertion_ABR(x, a.droite)
            return Noeud(v, 
                         gauche=a.gauche,
                         droite=nouveau_droite)

def recherche_ABR(x, a):
   """
   Répond True ou False selon que x est dans l'ABR a ou non.
   """

   if a is None:
        # Condition d'arrêt
        return False
   else:
        if x == a.valeur:
            return True
        elif x < a.valeur:
            return recherche_ABR(x, a.gauche)
        else:
            # x >= a.valeur, forcément
            return recherche_ABR(x, a.droite)

def taille(a):
   if a is None:
      return 0
   else:
      taille_gauche = taille(a.gauche)
      taille_droite = taille(a.droite)

      return 1 + taille_gauche + taille_droite

def hauteur(a):
   if a is None:
      return 0
   else:
      hauteur_gauche = hauteur(a.gauche)
      hauteur_droite = hauteur(a.droite)

      return 1 + max(hauteur_gauche, hauteur_droite)


def parcours_préfixe(a):
   if a is None:
      return
   else:
      print(a.valeur)
      parcours_préfixe(a.gauche)
      parcours_préfixe(a.droite)

a = Noeud(1, Noeud(2), Noeud(3))

parcours_préfixe(a)


def parcours_infixe(a):
   if a is None:
      return
   else:
      parcours_infixe(a.gauche)
      print(a.valeur)
      parcours_infixe(a.droite)

a = Noeud(1, Noeud(2), Noeud(3))

parcours_infixe(a)


def parcours_postfixe(a):
   if a is None:
      return
   else:
      parcours_postfixe(a.gauche)
      parcours_postfixe(a.droite)
      print(a.valeur)

a = Noeud(1, Noeud(2), Noeud(3))

parcours_postfixe(a)

def maximum(a):
   if a.gauche is None and a.droite is None:
      # C'est une feuille !
      return a.valeur
   else:
        maxi = a.valeur
        if a.gauche is not  None:
            maxi = max(maxi, maximum(a.gauche))
        if a.droite is not None:
            maxi = max(maxi, maximum(a.droite))

        return maxi

def minimum(a):
   if a.gauche is None and a.droite is None:
        # C'est une feuille !
        return a.valeur
   else:
        mini = a.valeur
        if a.gauche is not None:
            mini = min(mini, minimum(a.gauche))
        if a.droite is not None:
            mini = min(mini, minimum(a.droite))

        return mini

print("Le mini est " ,minimum(a))
print("Le max est " ,maximum(a))