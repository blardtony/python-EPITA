#Files 

#Exemples 1 

class File:

	def __init__(self):
		self.valeurs = []

	def enfiler(self, valeur):
		self.valeurs.append(valeur)

	def defiler(self):
		if self.valeurs:
			return self.valeurs.pop(0)

	def estVide(self):
		return self.valeurs == []

	@property
	def longueur(self):
		return len(self.valeurs)


	def __str__(self):
		ch = "\nEtat de la file:\n"
		for x in self.valeurs:
			ch +=  str(x) + " "
		return ch

q = File()
q.enfiler(9)
q.enfiler(2)
q.enfiler(5)

print(q)

q.defiler()
q.enfiler(7)

print("La file est-elle vide: ", q.estVide())

print(q)
print("Longueur de la file:", q.longueur)


#Exemple 2 Problème Josèphe

class Maillon:

	def __init__(self, valeur, precedent=None, suivant=None):
		self.valeur = valeur
		self.precedent = precedent
		self.suivant = suivant




class File2:

	def __init__(self):
		self.longueur = 0
		self.debut = None
		self.fin = None

	def enfiler(self, valeur):
		if self.longueur == 0:
			self.debut = self.fin = Maillon(valeur)
		else:
			self.fin = Maillon(valeur, self.fin)
			self.fin.precedent.suivant = self.fin
		self.longueur += 1


	def defiler(self):
		if self.longueur > 0:
			valeur = self.debut.valeur
			if self.longueur > 1:
				self.debut = self.debut.suivant
				self.debut.precedent = None
			else:
				self.debut = self.fin = None
			self.longueur -= 1
		return valeur


	def estVide(self):
		return self.longueur == 0




	def __str__(self):
		ch = "\nEtat de la file:\n"
		maillon = self.debut
		while maillon != None:
			ch +=  str(maillon.valeur) + " "
			maillon = maillon.suivant
		return ch




def josephe(listePersonnes, module):
	f = File2()
	for personne in listePersonnes:
		f.enfiler(personne)

	while not(f.estVide()):
		for _ in range(module-1):
			f.enfiler(f.defiler())
		p = f.defiler()

	return p


print(josephe( ['Antoine', 'Béatrice', 'Camille', 'Damien', 'Emile'], 3))