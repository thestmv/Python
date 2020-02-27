# Harjoitukset 4
# Tehtävä 7
# Syötteen pilkkoja
#
# () {} [] <>
# string_wrapper.py


print("Hello! I wrap strings into lines.")
print("Please, enter a string:")

syote = input()

print("Please, enter line length:")

merkkimaara = int(input())

#Välilyönnin tarkistaja
t = syote.split(" ")
if len(t) > 1:
    print("Error!")
elif(merkkimaara <= 0):
    print("Error!")
#Tulostetaan merkkijonot tietty määrä merkkejä kerrallaan
else:
    for i in range(0, len(syote), merkkimaara):
        print(syote[i:i+merkkimaara])

'''
else:
    for i in range(0, len(syote), merkkimaara):
        print(syote[i:4])
        '''