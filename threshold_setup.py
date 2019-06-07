import gmpy2
import hashlib
from settings import *
from securegroups import *
from generate_cyclic_group import *

generate_group()

#creates shared keys for number of tellers
def threshold():
	teller_keys = []

	for i in range(tellers):
		teller_keys.append(generate_keys())

	return teller_keys

#from shared keys compute
def compute_election_pk(keys):
	pkT = 1

	for i in keys:
		pkT *= i['pk'].value

	return pkT

# keys = threshold()
# print(keys[0])
# compute_election_pk(keys)


def get_hash_of_elements(*args):
	concat = ''
	for arg in args:
		concat += str(arg)

	concat = concat.encode('UTF-8')
	hashed_hex = hashlib.sha256(concat).hexdigest()
	# print(int(hashed_hex, 16))
	return int(hashed_hex, 16)

def proof_of_knowledge_sk(pk, sk):
	g = sk.parameters.g
	p = sk.parameters.p
	r = Element(type_Z)
	z = Element(type_Z)
	a = Element(type_G)
	set_random_value(r)

	a.value = gmpy2.powmod(g, r.value, p)
	hashed = get_hash_of_elements(g, pk.value, a.value)
	z.value = r.value + hashed + sk.value
	proof = PoK(a, z)

	print('Proof:::: a: ', proof.a.value, 'b: ', proof.z.value)
	return proof


g = generate_keys();

proof_of_knowledge_sk(g['pk'], g['sk'])

