from settings import *
from data_structures import *
from helpers import get_hash_of_elements, add_el, mul_el

def proof_of_knowledge_sk(pk, sk):
	"""
	prove knowledge of exponent of PK=g^{sk}
	returns PoK object
	"""
	g = sk.parameters.g
	p = sk.parameters.p
	r = El(type_Z)
	z = El(type_Z)
	a = El(type_G)
	set_random_value(r)

	a.value = gmpy2.powmod(g, r.value, p)
	hashed = get_hash_of_elements(g, pk.value, a.value)
	mul_el(z, hashed, sk.value)
	add_el(z, z.value, r.value)
	proof = PoK(a, z)

	return proof

def verify_knowledge_sk(pk, proof):
	"""
	verify given PoK knowledge
	returns true/false
	"""
	g = pk.parameters.g
	p = pk.parameters.p
	cmp1 = El(type_G)
	cmp2 = El(type_G)

	hashed = get_hash_of_elements(g, pk.value, proof.a.value)
	cmp1.value = gmpy2.powmod(g, proof.z.value, p)
	cmp2.value = gmpy2.powmod(pk.value, hashed, p)
	mul_el(cmp2, proof.a.value, cmp2.value)

	return cmp1.value == cmp2.value