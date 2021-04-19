#Dictionnaire
#dictionnaire en Python va  permettre de rassembler des éléments mais ceux-ci seront identifiés par une clé
mon_dictionnaire = {
    "voiture": "véhicule à quatre roues", 
    "vélo": "véhicule à deux roues"
}

print(mon_dictionnaire["voiture"]) # Affiche véhicule à quatre roues

mon_dictionnaire["tricycle"] = "véhicule à trois roues"

print(mon_dictionnaire) #Affiche {'voiture': 'véhicule à quatre roues','vélo': 'véhicule à deux roues','tricycle': 'véhicule à trois roues'}

print(type(mon_dictionnaire)) # Affiche dict

nombre_de_roues = {"voiture": 4, "vélo": 2}

print(type(nombre_de_roues)) # Affiche dict

print(nombre_de_roues["vélo"]) # Affiche 2


for i in nombre_de_roues.items():
    print(i)

for cle, valeur in nombre_de_roues.items():
    print("l'élément de clé", cle, "vaut", valeur)