# Harjoitukset 5
# Tehtävä 4
# Kokonaislukujen listahallinnointi
#
# int_list_controller.py


def printing():
    #print(lista1)
    if not lista1:
        print(lista1)
    else:
        print(lista1)

def summing(lista1):
    total = 0
    for ele in range(0, len(lista1)): 
        total = total + lista1[ele]
    print(total)
    
def stopper():
    exit()

print("Hello! I control a list.")

jatketaanko = True


lista1 = []
while jatketaanko:
    print("Please, enter a command:")


    reg = input()
    a,b=reg[:3],reg[4:]

    if(reg == "print"):
        printing()
    elif(reg == "exit"):
        stopper()
    elif(reg == "sum"):
        summing(total)
    elif(reg == "add"+reg):
        print()
    if all((a.isalpha(), b.isdigit())):
        lista1.append(reg[4:])
        print(lista1)
        #print(reg)
        
        
        