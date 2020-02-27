# Harjoitukset 4
# Tehtävä 4
# merkkijojon pituuksien vertailija
#
# () {} [] <>
# string_length_comparator.py


print("Hello! I compare the lengths of two strings.")
print("Please, enter the first string:")

merkkijono1 = input()

print("Please, enter the second string:")

merkkijono2 = input()

#Käytetään metodia len() merkkijonon pituuksien vertailuun
if len(merkkijono1) < len(merkkijono2):
    print('"'+merkkijono1 +'" is shorter than "'+ merkkijono2+'".')
elif len(merkkijono1) > len(merkkijono2):
    print('"'+merkkijono1 +'" is longer than "'+ merkkijono2+'".')
elif len(merkkijono1) == len(merkkijono2):
    print('"'+merkkijono1 +'" is as long as "'+ merkkijono2+'".')
    
    