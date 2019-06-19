from settings import *
from helpers import set_random_value

#returns dictionary with public and secret key from parameters
def generate_keys():
	PK = Element(type_G)
	SK = Element(type_Z)
	g = PK.parameters.g
	p = PK.parameters.p

	set_random_value(SK)
	PK.value = gmpy2.powmod(g, SK.value, p)
	print('Your public key is:', PK.value, 'Your secret key is:', SK.value)
	
	return {'pk' : PK, 'sk' : SK}