#4. Euclidean distance function #2
# euclideandistancefunction5.py

# Kirjoita toiminto nimeltä "print_distance", joka:
# *Vastaanottaa kaksi parametria p1 ja p2.
#	*Näiden oletetaan olevan tupleja tai luetteloita, jotka kuvaavat koordinaattiarvoja: 
#	p1 [0] on x- ja p1 [1] on p1: n y-koordinaatti ja 
#	p2: lla on samanlainen rakenne.
# *Laskee ja tulostaa Euklidinen etäisyys p1: n ja p2: n välillä.
#	*Tulostusmuoto: "P1: n ja p2: n välinen etäisyys on d", jossa p1 ja p2 ilmaisevat koordinaatit muodossa (x, y) 
#	ja d on etäisyys 2 tarkkuuden desimaalilla.
#	*Käytä jotakin muotoiltua tulostusta (esimerkiksi f-jouset tai muoto-toiminto). 
#	Älä käytä pyöreää toimintoa.
# Euclidean distance function

def print_distance(p1,p2):
	import math
	dist = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
	print("Distance between " + str(p1) + " and " + str(p2) + " is " + str(round(dist,2)))