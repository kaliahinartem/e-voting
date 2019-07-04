import gmpy2
import string
import time
from settings import *
from data_structures import *
from helpers import *
from generate_cyclic_group import generate_group
from keygen import generate_keys
"""
USAGE

> from generate_cyclic_group import generate_group
> from keygen import generate_keys
> 
> generate_group();
> keys = generate_keys();
> int_to_encr = 309458309458389475209385023498502349582304958
> str_to_encr = "æß12342µF±__TEST"
> pk = keys.pk
> sk = keys.sk
> int_cipher = elgamal_enc_int(pk, int_to_encr)
> print(int_cipher)
Ciphertext:
	a = 1123756425208646034224176028234154716361229869322586358577512270908970262777376909109683240630726079641939501532878384069175490697877181245293131352457883
	b = 939751253080357477385990056160177651041763792171527449734638095527600748817035938885720372864895531549254408139511574887150501567233080262088915792411238
> str_cipher = elgamal_enc(pk, str_to_encr)
> print(str_cipher[0]) #prints ciphertext for the first symbol in string
Ciphertext:
	a = 16185737975024154465612711716309427101979699714164496998105470342962622290305802935363375752842169516886647093975362568848736495948038851725716450457839160
	b = 21869694559807185562194195103433119464475213324463987927415330432130187855929759484009971398112449770246889074053359729451136499387922694974699164503637625
> decr_int = elgamal_dec_int(sk, int_cipher)
> print(decr_int)
309458309458389475209385023498502349582304958
> decr_str = elgamal_dec(sk, str_cipher)
æß12342µF±__TEST

"""

def elgamal_enc_int(pk, message):
	"""
	elgamal encryption of INTEGER (message should be int type)
	returns Cipher object with (a, b) encryption terms
	"""
	p = pk.parameters.p
	g = pk.parameters.g
	cipher = Cipher(El(type_G), El(type_G))
	r = El(type_Z)
	m = El(type_Z)
	m.value = message

	set_random_value(r)
	cipher.a.value = gmpy2.powmod(g, r.value, p)
	cipher.b.value = gmpy2.powmod(pk.value, r.value, p)
	mul_el(cipher.b, cipher.b.value, message)

	return cipher


def elgamal_enc(pk, message):
	"""
	elgamal encryption of STRING
	returns array of ciphers for each ascii symbol in the string
	"""
	if type(message) is not str:
		raise TypeError('String is required')

	ciphers_arr = []

	for symbol in message:
		num_representation = string_to_number(symbol)
		ciphers_arr.append(elgamal_enc_int(pk, num_representation))

	return ciphers_arr

def elgamal_dec_int(sk, cipher):
	"""
	elgamal decryption of given ciphertext
	returns decrypted INTEGER
	"""
	p = sk.parameters.p
	g = sk.parameters.g
	msg = El(type_G)

	msg.value = gmpy2.powmod(cipher.a.value, sk.value, p)
	div_el(msg, cipher.b.value, msg.value)

	return msg.value


def elgamal_dec(sk, cipher_arr):
	"""
	decrypts array with ciphertexts and returns decrypted STRING
	"""
	plaintext = ''

	for cipher in cipher_arr:
		decrypted_symbol = number_to_string(elgamal_dec_int(sk, cipher))
		plaintext += decrypted_symbol

	return plaintext
