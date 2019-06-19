from settings import *
from helpers import set_random_value, mul_el, div_el

#elgamal encryption of given integer
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

#elgamal decryption of given ciphertext
#returns decrypted integer
def elgamal_dec_int(sk, cipher):
	p = sk.parameters.p
	g = sk.parameters.g
	msg = Element(type_G)

	msg.value = gmpy2.powmod(cipher.a.value, sk.value, p)
	div_el(msg, cipher.b.value, msg.value)

	return msg.value

#elgamal encryption of string
#returns array of ciphers for each ascii symbol in the string
def elgamal_enc(pk, message):
	if type(message) is not str:
		raise TypeError('String is required')

	cipher_arr = []

	for symbol in message:
		num_representation = string_to_number(symbol)
		cipher_arr.append(elgamal_enc_int(pk, num_representation))

	return cipher_arr


#decrypts string given array with ciphertexts for each symbol
def elgamal_dec(sk, cipher_arr):
	plaintext = ''

	for cipher in cipher_arr:
		decrypted_symbol = number_to_string(elgamal_dec_int(sk, cipher))
		plaintext += decrypted_symbol

	return plaintext