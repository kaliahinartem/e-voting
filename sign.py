import gmpy2
from settings import *
from data_structures import *
from helpers import *

"""
USAGE
> from generate_cyclic_group import generate_group
> from keygen import generate_keys
> from elgamal import elgamal_enc_int
> generate_group(512);
> keys = generate_keys();
> int_to_encr = 309458309458389475209385023498502349582304958
> pk = keys.pk
> sk = keys.sk
> int_cipher = elgamal_enc_int(pk, int_to_encr)
> signature = sign(int_cipher, sk)
> print(signature)
Signature:
	k = 1230043279569536024001389511804641301711557998624482303125903964376804089428104801653636150176643087080728237816469773304919498726511180996181768741130329
	s = 3753651109088328727676738319469318294814766387873591464366293726646998122828522500522349702903083807819561223085801049884690100926401764933934435181310493
> verification = verify_sign(signature, int_cipher, pk)
> print(verification)
True

"""

def sign(message, sk):
	"""
	signs given message with private key
	message can be any type
	returns Signature object
	"""
	g = sk.parameters.g
	p = sk.parameters.p
	r = El(type_Z)
	k = El(type_G)
	s = El(type_Z)
	set_random_value(r)
	hashed = get_hash_of_elements(message)
	k.value = gmpy2.powmod(g, r.value, p)
	mul_el(s, hashed, sk.value)
	add_el(s, r.value, s.value)

	return Signature(k, s)


def verify_sign(sign, message, pk):
	"""
	verification of message signature
	returns true/false
	"""
	g = pk.parameters.g
	p = pk.parameters.p
	cmp1 = El(type_G)
	cmp2 = El(type_G)
	hashed = get_hash_of_elements(message)
	cmp1.value = gmpy2.powmod(g, sign.s.value, p)
	cmp2.value = gmpy2.powmod(pk.value, hashed, p)
	mul_el(cmp2, sign.k.value, cmp2.value)

	return cmp2.value == cmp1.value




