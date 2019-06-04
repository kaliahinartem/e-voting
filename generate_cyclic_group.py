import gmpy2
import time

security_level = 256
parameters = {
	'p': None,
	'g': None,
	'q': None
}

#returns a uniformly distributed random integer between 0 and 2**nBits - 1. 
def get_random_up_to_nbits(nBits):
	rand_state = gmpy2.random_state(int(time.time()*1000.0))
	r = gmpy2.mpz_urandomb(rand_state, nBits)
	return r

#returns a uniformly distributed random integer between 0 and max.
def get_random_up_to(max):
	rand_state = gmpy2.random_state(int(time.time()*1000.0))
	r = gmpy2.mpz_random(rand_state, max)
	return r

#generates p, q, and g parameters
def generate_group():
	global parameters

	parameters['q'] = get_random_up_to_nbits(security_level)

	#find primes p and q such as p = 2q + 1
	while True:
	 	parameters['q'] = gmpy2.next_prime(parameters['q'])
	 	parameters['p'] = parameters['q'] * 2 + 1
	 	if gmpy2.is_bpsw_prp(parameters['p']):
	 		break

	#find generator
	while True:
		parameters['g'] = get_random_up_to(parameters['p'])
		if gmpy2.powmod(parameters['g'], parameters['q'], parameters['p']) == 1:
			break

def test_group_values(params):
	if gmpy2.is_bpsw_prp(params['p']) and gmpy2.is_bpsw_prp(params['q']):
		print('P and Q are primes')
	else:
		print('Not primes')


generate_group()
test_group_values(parameters)
for key, val in parameters.items():
	print(key, ': ', val)