# Harjoitukset 4
# Tehtävä 6
# Syötteen tulostaja
#
# () {} [] <>
# string_triangle.py


print("Hello! I print a triangle made of prefixes of a string.")
print("Please, enter a string:")
syote = input()
pituus = len(syote)

#Välilyönnin tarkistaja
t = syote.split(" ")
if len(t) > 1:
    print("Error!")
else:
    #Silmukka laskee rivien määrän sanan pituudesta
    for rivi in range(pituus):
        #Laskee sarakkeiden määrän sanan pituudesta
        for sarake in range(rivi+1):
            #Tulostaa syötteen alottaen indeksistä 0
            print(syote[sarake],end="")
        print()

