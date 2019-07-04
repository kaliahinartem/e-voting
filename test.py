from elgamal import *

def test_elgamal_enc_int():

	for k in range (1, 10):
		keys = generate_keys()

		for i in range (1, 30):
			int_to_encrypt = get_random_in_range(10, 429380)
			for b in range (0, 5000000):
				a = 100
			print ('Integer for encryption: ', int_to_encrypt)
			decrypted_in_place = elgamal_dec_int(keys.sk, elgamal_enc_int(keys.pk, int_to_encrypt))
			result = int_to_encrypt == decrypted_in_place
			if result:
				print('Encr-decr successful!', int_to_encrypt, '-->', decrypted_in_place)
			else:
				print('Error!')

	# elgamal_encrypt_integer = elgamal_enc_int(keys.pk, 10843928409375912850921834897798)
def generate_random_string():
	string_of_symbols = string.printable
	random_length = get_random_in_range(1, 25)
	rand_str = ''
	for i in range (0, random_length):
		rand_str += string_of_symbols[get_random_in_range(0, len(string_of_symbols) - 1)]
		time.sleep(0.01)

	return rand_str


def test_elgamal_enc():
	for k in range (1, 10):
		generate_group()
		keys = generate_keys()

		for i in range (1, 30):
			str_to_encrypt = generate_random_string()
			time.sleep(0.01)
			# print ('Str for encryption: ', str_to_encrypt)
			decrypted_in_place = elgamal_dec(keys.sk, elgamal_enc(keys.pk, str_to_encrypt))
			result = str_to_encrypt == decrypted_in_place
			if result:
				print('Encr-decr successful!')
			else:
				raise TypeError('ERROR!')

	print('ALL TESTS ARE successful!!!')


test_elgamal_enc();