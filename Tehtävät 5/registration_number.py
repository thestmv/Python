# Harjoitukset 5
# Tehtävä 1
# Rekisteritunnus 
#
#
# registration_number.py


print("Hello! Just checking registration numbers.")
print("Please, enter a registration number:")



valid="ABC-123"

reg = input()
mark = "-"


try:
    a,c,b=reg[:3],reg[3] ,reg[4:]
    if all((a.isupper(), b.isdigit(), len(a)== 3,len(b)== 3)):
        if(c == "-"):
            print('"'+reg+'"'+ " is valid.")
        else:
            print('"'+reg+'"'+ " is invalid.")
    else:
        print('"'+reg+'"'+ " is invalid.")
except IndexError:
    print('"'+reg+'"'+ " is invalid.")