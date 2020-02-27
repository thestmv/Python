# commandlineparameters2.py
# Sorted command line parameters
# Kirjoita Python-ohjelma, joka tulostaa vastaanotetut komentoriviparametrit kahdesti: 
# Kerran nousevassa aakkosjärjestyksessä, sitten tyhjä rivi ja sitten kerran alenevassa aakkosjärjestyksessä.

# Huomaa: Katsomme, että todelliset komentoriviparametrit alkavat ohjelman nimen jälkeen; 
# joten älä sisällytä sitä tuotokseen.

# Esim. Jos tallennat koodisi tiedostoon nimeltä "task.py" ja 
# suoritat sen tavalla python "task.py yksi kaksi kolme neljä", odotettu tulos on:
# https://www.pythonforbeginners.com/argv/more-fun-with-sys-argv
'''
import sys


argv_len = len(sys.argv)
x = sys.argv

print(sys.argv)
print(argv_len)
print sorted(x) 
'''

#import sys

#aakkosjärjestyksessä
#ascending = sorted(sys.argv[1:])
#käänteisessä aakkosjärjestyksessä
#descending = sorted(sys.argv[1:], reverse=True)



#ascending = " \n".join(sorted(sys.argv))
#descending = " \n".join(sorted(sys.argv))

#print(ascending)
#print(descending)
#print(sys.argv[1:])

#print(ascending)
import sys
ascending = sorted(sys.argv[1:])
descending = sorted(sys.argv[1:], reverse=True)
print("\n".join(ascending))
print()
print("\n".join(descending))

     
'''
#print(descending)
argv_len = len(sys.argv)
for i in range(1, argv_len):
    #tmp_argv = sys.argv[i]
    #print(ascending)
    print(str(sys.argv[i:]))
'''
'''
argv
print(argv)
    tmp_argv = sys.argv[i]
    print(str(i)+": "+str(tmp_argv))
    '''
'''
# List 
x = ['q', 'w', 'r', 'e', 't', 'y'] 
print(sorted(x))

# Tuple 
x = ('q', 'w', 'e', 'r', 't', 'y') 
print(sorted(x))

# String-sorted based on ASCII translations 
x = "python"
print(sorted(x))

# Dictionary 
x = {'q':1, 'w':2, 'e':3, 'r':4, 't':5, 'y':6} 
print(sorted(x))

# Set 
x = {'q', 'w', 'e', 'r', 't', 'y'} 
print(sorted(x))

# Frozen Set 
x = frozenset(('q', 'w', 'e', 'r', 't', 'y')) 
print(sorted(x))
'''
'''
for i in range(1, argv_len):
    #print(chr(luku1), end='')
    tmp_argv = sys.argv[i]
    print(str(i)+": "+str(tmp_argv)+" (length: "+str(len(tmp_argv))+")")

'''

