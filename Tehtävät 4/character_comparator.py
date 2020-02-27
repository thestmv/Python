# Harjoitukset 4
# Tehtävä 5
# indeksiarvojen tutkija
#
# () {} [] <>
# character_comparator.py


print("Hello! I compare two characters of a string.")
print("Please, enter string:")
syote = input()

print("Please, enter the first position:")

ekapaikka = int(input())

print("Please, enter the second position:")
tokapaikka = int(input())
'''
print(syote[ekapaikka])
print(syote[tokapaikka])
'''
'''
syote[ekapaikka] = eka_kirjain
syote[len(syote) -tokapaikka] = toka_kirjain
'''
# Try-exept rakenne Index errorin varalta
try:
    if(syote[ekapaikka] == syote[tokapaikka]):
        print('"'+syote[ekapaikka]+'"'+" is equal to"+' "'+ syote[tokapaikka]+'".')
    elif(syote[ekapaikka] != syote[tokapaikka]):
        print('"'+syote[ekapaikka]+'"'+" is different from "+'"'+ syote[tokapaikka]+'".')
    else:
        print("Error!")
except IndexError:
    print("Error!")


#print(range(ekapaikka,tokapaikka))
