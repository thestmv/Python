# commandlineparameters.py
#
# Kirjoita Python-ohjelma, joka tulostaa vastaanotetut komentoriviparametrit muodossa 
# "i: par (pituus: len)", 
# missä lihavoidut arvot ovat (1) parametrin indeksi, (2) itse parametri ja ( 3) vastaavasti parametrin pituus.
#
# Huomaa: Katsomme, että todelliset komentoriviparametrit alkavat ohjelman nimen jälkeen; joten älä sisällytä 
# sitä tuotokseen.
# Esim. Jos tallennat koodisi tiedostoon nimeltä "task.py" ja suoritat sen tavalla python 
# "task.py one two three ", odotettu tulos on
# commandlineparameters.py
'''
par = "one"
i = 1
length = len(par)

def task(i, par, length):
    if len(par) < length:
        print(str(i)+": "+str(par)+" (length: "+str(len(par))+")",end='')
    print("1: "+str(par)+" (length: "+str(len(par))+")")
    print("1: "+str(par)+" (length: "+str(len(par))+")")
'''

import sys


argv_len = len(sys.argv)
for i in range(1, argv_len):
    #print(chr(luku1), end='')
    tmp_argv = sys.argv[i]
    print(str(i)+": "+str(tmp_argv)+" (length: "+str(len(tmp_argv))+")")
    
'''
import sys
# get command line argument length.
argv_len = len(sys.argv)
print('there are ' + str(argv_len) + ' arguments.')
# loop in all arguments.
for i in range(argv_len):
  tmp_argv = sys.argv[i]
  # print out argument index and value.
  print(str(i))
  print(tmp_argv)
  print('argv ' + str(i) + ' = ' + tmp_argv)
  '''
'''
def task(one, two, three):
    print("1: "+str(one)+" (length: "+str(len(one))+")")
    print("1: "+str(two)+" (length: "+str(len(two))+")")
    print("1: "+str(three)+" (length: "+str(len(three))+")")
'''

