from securegroups import *
from collections import OrderedDict
import string



class BytesIntEncoder:

    def __init__(self, chars: bytes = (string.ascii_letters + string.digits).encode()):
        num_chars = len(chars)
        translation = ''.join(chr(i) for i in range(1, num_chars + 1)).encode()
        self._translation_table = bytes.maketrans(chars, translation)
        self._reverse_translation_table = bytes.maketrans(translation, chars)
        self._num_bits_per_char = (num_chars + 1).bit_length()

    def encode(self, chars: bytes) -> int:
        num_bits_per_char = self._num_bits_per_char
        output, bit_idx = 0, 0
        for chr_idx in chars.translate(self._translation_table):
            output |= (chr_idx << bit_idx)
            bit_idx += num_bits_per_char
        return output

    def decode(self, i: int) -> bytes:
        maxint = (2 ** self._num_bits_per_char) - 1
        output = bytes(((i >> offset) & maxint) for offset in range(0, i.bit_length(), self._num_bits_per_char))
        return output.translate(self._reverse_translation_table).decode()


def create_tracking_numbers(number_of_voters, min_track, max_track):
	tracking_numbers = []
	i = 0
	while len(tracking_numbers) < number_of_voters:
		tracking_numbers.append(get_random_in_range(min_track, max_track))
		tmp = list(OrderedDict.fromkeys(tracking_numbers))
		if tmp != tracking_numbers:
			tracking_numbers = tmp
			continue

	return tracking_numbers

def elgamal_enc(pk, message):
	p = pk.parameters.p
	g = pk.parameters.g
	cipher = Cipher(Element(type_G), Element(type_G))
	r = Element(type_Z)
	encoder = BytesIntEncoder()
	message_to_int = encoder.encode(str(message).encode())

	set_random_value(r)

	cipher.a.value = gmpy2.powmod(g, r.value, p)

	cipher.b.value = gmpy2.powmod(pk.value, r.value, p)
	mul_el(cipher.b, cipher.b.value, message_to_int)

	print("a value: ", cipher.a.value, "b value:", cipher.b.value)

	return cipher

# def elgamal_dec(sk, cipher):
# 	p = sk.parameters.p
# 	g = sk.parameters.g

key = generate_keys()
elgamal_encryption(key['pk'], 'This is a message i want to encrypt')



