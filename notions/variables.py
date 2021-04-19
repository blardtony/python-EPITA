a = 10 # on affecte la constante entière 10 à la variable 'a'

c, b, s = 10, 9.3, 'nom' #Fait gagner du temps

del s # ou del(s) qui fonctionne aussi. del permet de rompre l'affectation

type(b), type(c) # type() permet d'afficher le type d'une variable

id(b), id(c) #adresse en mémoire vive d'une variable avec la fonction id()




#--------------Entier------------------------

a = 10**306 # ne pose pas de problème d'overflow
a**2        # là aussi, alors que pour le type float, il y en a un
type(a)
a = 0b10011001   # écriture en binaire après '0b' 
a = 0xABCEF      # écriture en hexadécimal après '0x'
a = int("120", base=3) # écriture en base quelconque (ici en base trois, ce qui donne 15)



#--------------Rééls------------------------

a = 1.0 # on affecte la constante réelle 1.0 à la variable 'a'
a = 2
type(a) #Affiche int
a = float(2)
type(a) #Affiche float



#--------------Complexes------------------------

c = complex(1,2)
d = 1 + 2j
print(c - d) # Affiche 0j
print( (1+1j)**2 / (1j) ) # Affiche 2+0j
print(c.real, c.imag) #Affiche 1.0 et 2.0



#--------------Booléens------------------------

test = True
print(test) # Affiche True
bool(0) # Affiche False
bool(13928) # Affiche True

bool(0)  # int
bool(0.) # float
bool("") # str
bool([]) # list
bool({}) # dict
bool(()) # tuple


#--------------Opérations------------------------

# + : addition
# - : soustraction
# * : multiplication
# / : division
# ** : élévation à la puissance
# // : division entière
# % : reste de la division entière	


#--------------Chaînes de caractères------------------------

mot = "Bonjour!"
mot = 'Bonjour!'  # même résultat
nombre = 102983
vide = "" # chaîne de caractère vide ou pas de caractère
aff = str(nombre)
print(nombre, aff) # Affiche 102983 102983

mot2 = "et "
mot2 *= 3
mot2 += "alors..."
print(mot2) #Affiche et et et alors...

mot3 = "Bonjour!"
print(mot3[-1], mot3[3:5], 'B' in mot) # Affiche ! jo True