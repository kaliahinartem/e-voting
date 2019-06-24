import gmpy2
from settings import *
from data_structures import *
from helpers import set_random_value

#returns Keys object with public and secret keys
def generate_keys():
	PK = Element(type_G)
	SK = Element(type_Z)
	g = PK.parameters.g
	p = PK.parameters.p

	set_random_value(SK)
	PK.value = gmpy2.powmod(g, SK.value, p)
	print(PK)
	print('Your public key is:', PK.value, 'Your secret key is:', SK.value)
	
	return Keys(PK, SK)

generate_keys();