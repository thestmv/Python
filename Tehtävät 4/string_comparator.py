# Harjoitukset 4
# Tehtävä 3
# Lause vertailija
#
# () {} [] <>
# string_comparator.py

print("Hello! I compare strings.")


#Määritellään syötteet vakioksi
LOPETUSLAUSE = "xyz"

jatketaanko = True

while jatketaanko:
    print("Please, enter the first string:")
    merkkijono1 = input()
    print("Please, enter the second string:")
    merkkijono2 = input()
    if(merkkijono1 == LOPETUSLAUSE and merkkijono2 == LOPETUSLAUSE):
        jatketaanko = False
    elif merkkijono1 == merkkijono2:
        print('"'+merkkijono1 +'" is equal to "'+ merkkijono2+'".')
    else:
        print('"'+merkkijono1 +'" is different from "'+ merkkijono2+'".')