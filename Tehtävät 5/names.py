# Harjoitukset 5
# Tehtävä 3
# Etunimen tunnistaja
#
# names.py
 

def printing():
    #print(lista1)
    if not lista1:
        return
    else:
        print(*lista1, sep = "\n")
def stopper():
    exit()


jatketaanko = True

lista1 = []
print("Hello! I detect and store names.")

while jatketaanko:
    print("Please, enter a name or a command:")
    reg = input()
    a,b=reg[0],reg[1:]
    
    if(reg == "print"):
        printing()
    elif(reg == "stop"):
        stopper()
    elif(a.isupper() and b.isalpha()):
        print("Accepted.")
        #Listaan lisääminen
        lista1.append(reg)
    elif(" " in reg):
        print("Rejected!")
    elif(b.isnumeric()):
        print("Rejected!")
    elif(a.isupper()):
        print("Accepted.")
        lista1.append(reg)
    else:
        print("Rejected!")
            
