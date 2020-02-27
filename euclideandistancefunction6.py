#4. Euclidean distance function #3
# euclideandistancefunction6.py

#Kirjoita funktio nimeltä print_distance, joka
# *Vastaanottaa kolme parametria p1, p2 ja prec.
#	*Kuten aikaisemmin, p1: n ja p2: n oletetaan olevan tupleja tai luetteloita, 
#	jotka kuvaavat koordinaattiarvoja.
#	*Parametrin prec oletetaan olevan positiivinen kokonaisluku, joka määrittelee tarkkuuden 
#	(tulostettavien desimaalien määrä). Määritä tarkkuuden oletusarvo 2.
# *Laskee ja tulostaa Euklidinen etäisyys p1: n ja p2: n välillä tarkkuuden desimaalin tarkkuudella.
#	*Tulostemuoto on "Etäisyys p1: n ja p2: n välillä desimaalin tarkkuudella on d", 
#	missä prec ilmaisee desimaalin lukumäärän.
#	ja d on etäisyys 2 tarkkuuden desimaalilla.
#	*Käytä uudelleen jotakin muotoiltua tulostustapaa (esim. F-jouset tai muoto-toiminto). 
#	Älä käytä pyöreää toimintoa.
# Euclidean distance function
# Distance between (0, 1) and (-1, -2) with 2 decimals is 3.16
# Distance between (0, 1) and (-1, -2) with 3 decimals is 3.162




#def print_distance(p1,p2,prec=2):
#	import math
#	dist = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
	#lause = 'Distance between {p1}. and {p2}. with {prec}. desimals is {dist}.'.format(p1,p2,prec,dist)
	#"%0.1f" % dist
	#lause = 'Distance between {} and {} with {} desimals is {}'.format(p1,p2,prec,dist)
#	lause = 'Distance between {} and {} with {} desimals is {:.'+prec+'.f}'.format(p1,p2,prec,dist)
	
	
	#print("Number", i, ":", format(num, 'VAR.2f')) # VAR needs to equal field_size

	#print('Number {i}: {num:{field_size}.2f}'.format(i=i, num=num, field_size=field_size))
	#print("Distance between " + str(p1) + " and " + str(p2) + " with "+ str(prec) + " desimals is "+ str(round(dist,prec)))
	#print("Distance between " + str(p1) + " and " + str(p2) + " with "+ str(prec) + " desimals is "+ str(round(dist,prec)))
	#print("Distance between " + str(p1) + " and " + str(p2) + " with "+ str(prec) + " desimals is "+ str(round(dist,2)))
#	print(lause)
def print_distance(p1,p2,prec=2):
	import math
	dist = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
	#lause = 'Distance between {p1}. and {p2}. with {prec}. desimals is {dist}.'.format(p1,p2,prec,dist)
	lause = 'Distance between {} and {} with {} desimals is {:.{prec}f}'.format(p1,p2,prec,dist,prec)
	#print( '{0} found the following floats: {1:.{digits}f}, {2:.{digits}f}, {3:.{digits}f}'.format(sName, fFirstFloat, fSecondFloat, fThirdFloat, digits=dNumDecimals))
	return(lause)
	
x1 = 0
y1 = 1
x2 = -1
y2 = -2
	
#prec = 3
p1 = (x1,y1)
p2 = (x2,y2)

print_distance(p1,p2,prec=5)
	
	
	
	
	