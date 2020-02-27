# Hello function #3
# 
# hellofunction4.py

# Kirjoita toiminto sayhello
# Vastaanottaa yhden parametrin, jonka oletus arvo on "anonymius"
# Tulostaa viestin "Hello 'parametri'!"
# -Vastaanottaa yhden parametrin, jonka oletusarvon tulisi olla "tuntematon".
# -Palauta muodon "Hello par!" Sring, jossa lihavoitu osa par on vastaanotettu parametri. 
# Tässä alatehtävässä parametri voi olla myös muun tyyppinen kuin merkkijono. 
# Voit kuitenkin olettaa, että parametri voidaan muuntaa merkkijonoksi kutsumalla str.

# Esimerkiksi. kutsu hello_string () palauttaa merkkijonon "Hei anonyymi!", ja 
# kutsu hello_string ("!!") merkkijono "Hei !!!". Lisäksi puhelu say_hello (2018) 
# tulostaa "Hei 2018!". Huomaa, kuinka tässä viimeisessä tapauksessa parametri oli kokonaisluku.

def hello_string(par="anonymous"):
	tervehdys = "Hello "
	huuto = "!"
	endpar = (tervehdys+par+huuto)
	print(tervehdys+par+huuto)
	return (par)




def hello_string(par="anonymous"):
	tervehdys = "Hello "
	huuto = "!"
	endpar = (tervehdys+str(par)+huuto)
	return (endpar)


hello_string()
	






