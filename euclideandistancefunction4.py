#4. Distance functions
# euclideandistancefunction4.py

# Lasketaan euklidinen etäisyys pisteiden välilläeuclideandistancefunction4
# Kirjoita toiminto nimeltä "etäisyys", joka:
# *Vastaanottaa kaksi parametria p1 ja p2.
#	*Näiden oletetaan olevan tupleja tai luetteloita, jotka kuvaavat 
#	koordinaattiarvoja: p1 [0] on x- ja p1 [1] n p1: n y-koordinaatti ja p2: lla on samanlainen rakenne.
# *Laskee ja palauttaa euklidisen etäisyyden p1 ja p2 välillä.
#	*Muista, että etäisyys (x1, y1) ja (x2, y2) on (x2 − x1) 2+ (y2 − y1) 2 −−−−−−−−−−−−−−−−−−− √ .
#	*Huomaa, että toimintosi ei pitäisi tulostaa mitään!
# Euclidean distance function

def distance(x1,y1,x2,y2):
  import math
  dist = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
  return dist:
  