import gmpy2
import time
import hashlib
import binascii
from settings import *
from data_structures import *


def get_random_up_to_nbits(nBits):
	#returns a uniformly distributed random integer between 0 and 2^nBits - 1
	rand_state = gmpy2.random_state(int(time.time()*1000.0))
	r = gmpy2.mpz_urandomb(rand_state, nBits)

	return r

def get_random_up_to(max):
	#returns a uniformly distributed random integer between 0 and max (excluding max)
	seed = int(time.time()*1000.0)
	rand_state = gmpy2.random_state(seed)
	r = gmpy2.mpz_random(rand_state, max)

	return r

def get_random_in_range(min, max):
	#returns a random integer in range [min, max]
	seed = int(time.time()*1000.0)
	rand_state = gmpy2.random_state(seed)
	r = gmpy2.mpz_random(rand_state, 1 + max - min)

	return min + r

def set_random_value(elem):
	#sets value field of an element object as a random value depending on the element type
	parameters = elem.parameters

	if elem.type == type_G:
		while True:
			elem.value = get_random_up_to(parameters.p)
			if gmpy2.powmod(elem.value, parameters.q, parameters.p) == 1:
				break
	else:
		elem.value = get_random_up_to(parameters.q)

def get_hash_of_elements(*args):
	#concatenates and hashes arguments passed to the function, returns hash in decimal representation
	concat = ''

	for arg in args:
		concat += str(arg)
	concat = concat.encode('UTF-8')
	hashed_hex = hashlib.sha256(concat).hexdigest()
	
	return int(hashed_hex, 16)

def add_el(result, el1, el2):
	"""
	adds 2 elements and sets result.value
	field to addition result, first argument should be be an El object
	2nd and 3rd argument - values to add
	"""
	p = result.parameters.p
	q = result.parameters.q

	result.value = gmpy2.add(el1, el2)
	result.value = (gmpy2.f_mod(result.value, p), gmpy2.f_mod(result.value, q))[result.type]

def sub_el(result, el1, el2):
	"""
	subtracts el1 - el2 elements and sets result.value
	field to subtraction result, first argument should be be an El object
	2nd and 3rd argument - values to subtract
	"""
	p = result.parameters.p
	q = result.parameters.q

	result.value = gmpy2.sub(el1, el2)
	result.value = (gmpy2.f_mod(result.value, p), gmpy2.f_mod(result.value, q))[result.type]

def mul_el(result, el1, el2):
	"""
	multiplies elements and sets result.value
	field to multiplication result, first argument should be be an El object
	2nd and 3rd argument - values to multiply
	"""
	p = result.parameters.p
	q = result.parameters.q

	result.value = gmpy2.mul(el1, el2)
	result.value = (gmpy2.f_mod(result.value, p), gmpy2.f_mod(result.value, q))[result.type]

def div_el(result, el1, el2):
	"""
	divides el1 on el2 (inverts el2 and multiplies them) and sets result.value
	field to division result, first argument should be be an El object
	2nd and 3rd argument - values to divide
	"""
	p = result.parameters.p
	q = result.parameters.q
	tmp = El(type_G, el2)

	tmp.value = (gmpy2.invert(tmp.value, p), gmpy2.invert(tmp.value, q))[result.type]
	result.value = gmpy2.mul(el1, tmp.value)
	result.value = (gmpy2.f_mod(result.value, p), gmpy2.f_mod(result.value, q))[result.type]

def string_to_number(string):
	#decodes string to number (may not work for some big integers)
	byte_str = string.encode("utf-8")
	byte_to_hex = binascii.hexlify(byte_str)
	integer = int(byte_to_hex, 16)

	return integer

def number_to_string(number):
	#decodes integer to a string
	formatted_number = format(number, "x")
	if len(formatted_number) % 2 == 1:
		formatted_number = '0' + formatted_number
	encoded_number = formatted_number.encode("utf-8")
	hex_number = binascii.unhexlify(encoded_number)
	string = hex_number.decode("utf-8")

	return string





