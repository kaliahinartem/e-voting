from settings import *
from data_structures import *
from helpers import get_random_up_to_nbits, get_random_up_to
import gmpy2
import time

#generates p, q, and g parameters and sets fields in global variable parameters
def generate_group(nBits):

	parameters.q = get_random_up_to_nbits(nBits)

	#find primes p and q such as p = 2q + 1
	while 1:
	 	parameters.q = gmpy2.next_prime(parameters.q)
	 	parameters.p = parameters.q * 2 + 1
	 	if gmpy2.is_bpsw_prp(parameters.p):
	 		break

	#find generator of the group
	while 1:
		parameters.g = get_random_up_to(parameters.p)
		if gmpy2.powmod(parameters.g, parameters.q, parameters.p) == 1:
			break

# def test_group_values(params):
# 	if gmpy2.is_bpsw_prp(params.p) and gmpy2.is_bpsw_prp(params.q):
# 		print('P and Q are primes')
# 	else:
# 		print('Not primes')