# Harjoitukset 4
# Tehtävä 1
# Arvosanat
#
#
# grader.py


print("Hello! I am a grader.")
print("Please, enter exam points:")

tentti_pisteet = int(input())

print("Please, enter bonus points:")

hyvitus = int(input())

kaikki_pisteet = tentti_pisteet + hyvitus

if(tentti_pisteet >= 12 and hyvitus < 4):
    if(kaikki_pisteet <= 11):
        print("I cannot grade you.")
    elif(kaikki_pisteet >= 12) and (kaikki_pisteet<=14):
        print("Your grade is 1.")
    elif(kaikki_pisteet >= 15) and (kaikki_pisteet<=17):
        print("Your grade is 2.")
    elif(kaikki_pisteet >= 18) and (kaikki_pisteet<=20):
        print("Your grade is 3.")
    elif(kaikki_pisteet >= 21) and (kaikki_pisteet<=22):
        print("Your grade is 4.")
    elif kaikki_pisteet >= 23:
        print("Your grade is 5.")
else:
    print("I cannot grade you.")