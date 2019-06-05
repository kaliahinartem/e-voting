from settings import *
from instances import *
from securegroups import *
import gmpy2
import time

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

generate_group()

# def test_group_values(params):
# 	if gmpy2.is_bpsw_prp(params['p']) and gmpy2.is_bpsw_prp(params['q']):
# 		print('P and Q are primes')
# 	else:
# 		print('Not primes')