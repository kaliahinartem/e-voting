import gmpy2
import string
import time
from settings import *
from data_structures import *
from helpers import *
from keygen import generate_keys
from generate_cyclic_group import generate_group


#elgamal encryption of given INTEGER
#returns Cipher object with (a, b) encryption terms
def elgamal_enc_int(pk, message):
	p = pk.parameters.p
	g = pk.parameters.g
	cipher = Cipher(Element(type_G), Element(type_G))
	r = Element(type_Z)
	m = Element(type_Z)
	m.value = message

	set_random_value(r)
	cipher.a.value = gmpy2.powmod(g, r.value, p)
	cipher.b.value = gmpy2.powmod(pk.value, r.value, p)
	mul_el(cipher.b, cipher.b.value, message)

	return cipher

#elgamal encryption of STRING
#returns array of ciphers for each ascii symbol in the string
def elgamal_enc(pk, message):
	if type(message) is not str:
		raise TypeError('String is required')

	cipher_arr = []

	for symbol in message:
		num_representation = string_to_number(symbol)
		cipher_arr.append(elgamal_enc_int(pk, num_representation))

	return cipher_arr

#elgamal decryption of given ciphertext
#returns decrypted INTEGER
def elgamal_dec_int(sk, cipher):
	p = sk.parameters.p
	g = sk.parameters.g
	msg = Element(type_G)

	msg.value = gmpy2.powmod(cipher.a.value, sk.value, p)
	div_el(msg, cipher.b.value, msg.value)

	return msg.value

#decrypts STRING given array with ciphertexts for each symbol
def elgamal_dec(sk, cipher_arr):
	plaintext = ''

	for cipher in cipher_arr:
		decrypted_symbol = number_to_string(elgamal_dec_int(sk, cipher))
		plaintext += decrypted_symbol

	return plaintext