import gmpy2
import time
from settings import *

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

#returns a uniformly distributed random integer between 0 and 2**nBits - 1. 
def get_random_up_to_nbits(nBits):
	rand_state = gmpy2.random_state(int(time.time()*1000.0))
	r = gmpy2.mpz_urandomb(rand_state, nBits)

	return r

#returns a uniformly distributed random integer between 0 and max.
def get_random_up_to(max):
	seed = int(time.time()*1000.0)
	rand_state = gmpy2.random_state(seed)
	r = gmpy2.mpz_random(rand_state, max)

	return r

def get_random_in_range(min, max):
	seed = int(time.time()*1000.0)
	rand_state = gmpy2.random_state(seed)
	r = gmpy2.mpz_random(rand_state, 1 + max - min)
	return min + r

#sets value field of an element object as a random value
def set_random_value(elem):
	parameters = elem.parameters

	if elem.type == type_G:
		while True:
			elem.value = get_random_up_to(parameters.p)
			if gmpy2.powmod(elem.value, parameters.q, parameters.p) == 1:
				break
	else:
		elem.value = get_random_up_to(parameters.q)

#concatenates and hashes arguments passed to the function, returns hash in decimal representation
def get_hash_of_elements(*args):
	concat = ''
	for arg in args:
		concat += str(arg)
	concat = concat.encode('UTF-8')
	hashed_hex = hashlib.sha256(concat).hexdigest()
	
	return int(hashed_hex, 16)

#generates dictionary with public and secret key
def generate_keys():
	PK = Element(type_G)
	SK = Element(type_Z)
	g = PK.parameters.g
	p = PK.parameters.p

	set_random_value(SK)
	PK.value = gmpy2.powmod(g, SK.value, p)
	print('Your public key is:', PK.value, 'Your secret key is:', SK.value)
	
	return {'pk' : PK, 'sk' : SK}

#adds 2 elements + mod p/q depending on the result type
#and sets result.value field to result, first argument should be be an Element object
#2nd and 3rd argument - values to add
def add_el(result, el1, el2):
	p = result.parameters.p
	q = result.parameters.q

	result.value = gmpy2.add(el1, el2)
	result.value = (gmpy2.f_mod(result.value, p), gmpy2.f_mod(result.value, q))[result.type]

#multiplies 2 elements similar to add_el function
def mul_el(result, el1, el2):
	p = result.parameters.p
	q = result.parameters.q

	result.value = gmpy2.mul(el1, el2)
	result.value = (gmpy2.f_mod(result.value, p), gmpy2.f_mod(result.value, q))[result.type]

#divides 2 elements similar to add_el function
def div_el(result, el1, el2):
	p = result.parameters.p
	q = result.parameters.q

	result.value = gmpy2.add(el1, el2)
	result.value = (gmpy2.f_mod(result.value, p), gmpy2.f_mod(result.value, q))[result.type]

