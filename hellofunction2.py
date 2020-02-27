# Hello function #2
# 
# hellofunction3.py

# Kirjoita toiminto sayhello
# Vastaanottaa yhden parametrin, jonka oletus arvo on "anonymius"
# Tulostaa viestin "Hello 'parametri'!"
# 
# 



def say_hello(par):
	tervehdys = "Hello "
	huuto = "!"
	print(tervehdys+par+huuto)
	maara = len(tervehdys+par+huuto)
	print("Printed",maara,"characters")
	return (maara)
	

say_hello("anonymous")
say_hello("programmers around the world")
say_hello("ladies and gentlemen")
say_hello("is also a song by Adele")

