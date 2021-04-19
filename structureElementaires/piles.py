#Piles

pile = []
pile.append(5)
pile.append(2)
pile.append(0)
pile.append(10)
                    
print(pile) # Affiche [5, 2, 0, 10]
a = pile.pop() 

print(a) # Affiche 10
print(pile) # Affiche [5, 2, 0]

print(pile[1])# Affiche 2


# Exemple Piles 

class Pile:

	def __init__(self):
		self.valeurs = []

	def empiler(self, valeur):
		self.valeurs.append(valeur)

	def depiler(self):
		if self.valeurs:
			return self.valeurs.pop()

	def estVide(self):
		return self.valeurs == []


	def __str__(self):
		ch = ''
		for x in self.valeurs:
			ch = "|\t" + str(x) + "\t|" + "\n" + ch
		ch = "\nEtat de la pile:\n" + ch
		return ch



p = Pile()
p.empiler(9)
p.empiler(2)
p.empiler(5)

print(p)

p.depiler()
p.empiler(7)

print(p.estVide())

print(p)



#Exemple 2 pile Polonaise

class Maillon:

	def __init__(self, valeur, suivant=None):
		self.valeur = valeur
		self.suivant = suivant



class Pile2:

	def __init__(self):
		self.taille = 0 # nombre d'assiettes dans la pile
		self.sommet = None


	def empiler(self, valeur):
		self.sommet = Maillon(valeur, self.sommet)
		self.taille += 1

	def depiler(self):
		if self.taille > 0:
			valeur = self.sommet.valeur
			self.sommet = self.sommet.suivant
			self.taille -= 1
			return valeur

	def estVide(self):
		return self.taille == 0




	def __str__(self):
		ch = "\nEtat de la pile:\n"
		sommet = self.sommet
		while sommet != None:
			ch += "|\t" + str(sommet.valeur) + "\t|" + "\n"
			sommet = sommet.suivant

		return ch






def prefixe(expression):
	pile = Pile2()
	for c in reversed(expression):
		if isinstance(c, int):
			pile.empiler(c)
			print(pile)
		else:
			a = pile.depiler()
			b = pile.depiler()
			pile.empiler(eval(str(a) + c + str(b)))
			print(pile)
	return pile.depiler()


r = prefixe(['+', '*', '-', '/', 10, 2, 4, 3, 6])
print(r)




