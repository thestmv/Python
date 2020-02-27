# Harjoitukset 4
# Tehtävä 2
# Suljeparit
#
# () {} [] <>
# pairs.py


print("Hello! I find pairs.")
print("Enter the first character:")

merkki1 = input()

print("Enter the second character:")

merkki2 = input()

if(merkki1 == "("and merkki2 == ")"):
    print('Characters "' + merkki1 +'" and "'+ merkki2 +'" are a pair.')
elif(merkki1 == "{"and merkki2 == "}"):
    print('Characters "' + merkki1 +'" and "'+ merkki2 +'" are a pair.')
elif(merkki1 == "["and merkki2 == "]"):
    print('Characters "' + merkki1 +'" and "'+ merkki2 +'" are a pair.')
elif(merkki1 == "<"and merkki2 == ">"):
    print('Characters "' + merkki1 +'" and "'+ merkki2 +'" are a pair.')
else:
    print('Characters "' + merkki1 +'" and "'+ merkki2 +'" are not a pair.')