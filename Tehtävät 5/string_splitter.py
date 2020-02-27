# Harjoitukset 5
# Tehtävä 2
# sanapilkkoja
#
# string_splitter.py




print("Hello! I split strings.")

jatketaan = True

while jatketaan:
    print("Please, enter a string:")
    syote = input()

    print("Please, enter a separator:")

    erotin = input()

    x = syote.split(erotin)

    if(erotin in syote):
        print(x)
    else:
        jatketaan = False
