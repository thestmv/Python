# Simple loops 
# simpleloops1.py
#
# Kirjoita toiminto nimeltä "print_ints", joka:
#-Vastaanottaa kolme parametria: n, k ja sep.
#	*n: n ja k: n odotetaan olevan kokonaislukuja, missä k> 0. Jos k ≤ 0, toiminto tulostaa 
#	"Laiton parametri k = k!" ja palauttaa, missä lihavoitu k on k: n todellinen arvo.
#	*k: lla tulisi olla oletusarvo 1 ja sep oletusarvolla "".
#-Tulostaa k: nnen kokonaisluvun välillä 0 ... n, molemmat päät mukaan lukien. Arvot erotetaan lähdössä sep.
#	*Esimerkiksi. Jos n = 4, k = 2 ja sep = "_", toiminnon tulisi tulostaa "0_2_4". 
#	Huomaa, että sep on vain arvojen välillä; Älä tulosta sitä ennen ensimmäistä tai viimeistä.
#	*n voi olla negatiivinen: esim. jos n = -5, k = 2 ja sep = "", ohjelman tulisi tulostaa "0 -2 -4".
#		*Huomaa, kuinka viimeisin painettu arvo oli -4: kun tulostat joka 2. arvo, seuraava arvo olisi ollut -6, 
#		joka jo ylitti sidotun n = -5.
# Huomaa, kuinka viimeisin painettu arvo oli -4: kun tulostat joka 2. arvo, seuraava arvo olisi ollut -6, joka jo ylitti sidotun n = -5.
#WETO: n ensimmäinen testi suorittaa kutsut print_ints (4, 2, "_"), print_ints 
#(-5, 2), print_ints (5, sep = "<") ja print_ints (2, 0). Odotettu tuotos on:


def print_ints(n=0,k=1,sep=0):

	if(k<=0):
		print("Illegal parameter k = "+str(k)+"!")
		return(k)
	if(sep == "_"):
		print(str(n)+"_"+str(k)+"_"+str(sep))
	if(n < 0):
		print(print(str(n)+"-"+str(k)+"-"+str(sep)))
	if(sep == "<"):
		for k in n:
			print(k * n)
			print(k)
			print("<")
	
	
n = 0
k = 2
sep = 4
	
print_ints(4,2,"<")