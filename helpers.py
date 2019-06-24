import gmpy2
import time
import hashlib
import binascii
from settings import *
from data_structures import *

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

get_hash_of_elements(1, 2, 3)

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

#divides 2 elements (inverts second element and multiplies
#it with the first one), then sets result.value to result of division
def div_el(result, el1, el2):
	p = result.parameters.p
	q = result.parameters.q
	tmp = Element(type_G, el2)

	tmp.value = (gmpy2.invert(tmp.value, p), gmpy2.invert(tmp.value, q))[result.type]
	result.value = gmpy2.mul(el1, tmp.value)
	result.value = (gmpy2.f_mod(result.value, p), gmpy2.f_mod(result.value, q))[result.type]

#decodes string to number (may not work for some big integers)
def string_to_number(string):
	byte_str = string.encode("utf-8")
	byte_to_hex = binascii.hexlify(byte_str)
	integer = int(byte_to_hex, 16)

	return integer

#decodes integer to a string
def number_to_string(number):
	formatted_number = format(number, "x")
	if len(formatted_number) % 2 == 1:
		formatted_number = '0' + formatted_number
	encoded_number = formatted_number.encode("utf-8")
	hex_number = binascii.unhexlify(encoded_number)
	string = hex_number.decode("utf-8")

	return string





