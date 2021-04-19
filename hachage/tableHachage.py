#Exemple 1 
#un ensemble de 256 caractères (l’alphabet ASCII)

def str_to_int ( s ) :
    n = 0
    for c in s :
        n = n * 256 + ord(c)
    return n

def hachage ( s ) :
    return str_to_int(s)%255



print(hachage("Blop"))


#Exemple 2 

def hash_key( key, m):
    return key % m

m = 7

print(f'The hash value for 3 is {hash_key(3,m)}')
print(f'The hash value for 2 is {hash_key(2,m)}')
print(f'The hash value for 9 is {hash_key(9,m)}')
print(f'The hash value for 11 is {hash_key(11,m)}')
print(f'The hash value for 7 is {hash_key(7,m)}')

