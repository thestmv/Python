# commandlineparameters3.py
#Sorted command line parameters #2

#Kirjoita Python-ohjelma, joka tulostaa saamansa komentoriviparametrit nousevassa 
#aakkosjärjestyksessä muodossa "par (hakemisto: i)", missä lihavoidut arvot ovat 
#(1) parametri ja (2) alkuperäinen hakemisto (ennen lajittelua) ) vastaavasti. 
#Jos samanlaisia parametreja on useita, ne tulisi tulostaa indeksiensä nousevassa järjestyksessä.

#Huomaa: Katsomme, että todelliset komentoriviparametrit alkavat ohjelman nimen jälkeen; 
#joten älä sisällytä sitä tuotokseen.

#Esim. Jos tallennat koodisi tiedostoon nimeltä "task.py" ja suoritat sen tavalla python 
#"task.py yksi kaksi kolme neljä", odotettu tulos on:
# commandlineparameters3.py


import sys
'''
ascending = sorted(sys.argv[1:])
descending = sorted(sys.argv[1:], reverse=True)
print("\n".join(ascending)+" index:")
print()
print("\n".join(descending)+" index:")
'''
#tmp_argv = sys.argv[i]
#ascending = sorted("".join(tmp_argv)+" (index: "+sys.argv[i]+")")

argv_len = len(sys.argv)
for i in range(1, argv_len):
    #print(chr(luku1), end='')
    tmp_argv = sys.argv[i]
    print(sorted("".join(tmp_argv)+" (index: "+str(argv_len)+")"))
    #print(ascending)