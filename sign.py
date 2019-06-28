import gmpy2
from settings import *
from data_structures import *
from helpers import *

#signs given message with private key
#message can be any type
#returns Signature object
def sign(message, sk):
	g = sk.parameters.g
	p = sk.parameters.p
	r = Element(type_Z)
	k = Element(type_G)
	s = Element(type_Z)
	tmp = Element(type_Z)
	set_random_value(r)
	hashed = get_hash_of_elements(message)
	k.value = gmpy2.powmod(g, r.value, p)
	mul_el(tmp, hashed, sk.value)
	add_el(s, r.value, tmp.value)

	return Signature(k, s)


#verification of message signature
def verify_sign(sign, message, pk):
	g = pk.parameters.g
	p = pk.parameters.p
	cmp1 = Element(type_G)
	cmp2 = Element(type_G)
	hashed = get_hash_of_elements(message)
	cmp1.value = gmpy2.powmod(g, sign.s.value, p)
	cmp2.value = gmpy2.powmod(pk.value, hashed, p)
	mul_el(cmp2, sign.k.value, cmp2.value)

	return cmp2.value == cmp1.value




