import gmpy2
import time
from settings import *
from instances import *
	
#returns a uniformly distributed random integer between 0 and 2**nBits - 1. 
def get_random_up_to_nbits(nBits):
	rand_state = gmpy2.random_state(int(time.time()*1000.0))
	r = gmpy2.mpz_urandomb(rand_state, nBits)
	return r

#returns a uniformly distributed random integer between 0 and max.
def get_random_up_to(max):
	print(max)
	rand_state = gmpy2.random_state(int(time.time()*1000.0))
	r = gmpy2.mpz_random(rand_state, max)
	return r

#sets value field of an element object as a random value
def set_random_value(elem):
	parameters = elem.parameters
	if elem.type == type_G:
		while True:
			elem.value = get_random_up_to(parameters['p'])
			if gmpy2.powmod(elem.value, parameters['q'], parameters['p']) == 1:
				break
	else:
		elem.value = get_random_up_to(parameters['q'])

#generates dictionary with public and secret key
def generate_keys():
	PK = Element(type_G)
	SK = Element(type_Z)
	set_random_value(SK)
	PK.value = gmpy2.powmod(PK.parameters['g'], SK.value, PK.parameters['p'])
	print('Your public key is:', PK.value, 'Your secret key is:', SK.value)
	return {'pk' : PK, 'sk' : SK}