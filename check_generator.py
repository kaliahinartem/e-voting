import sys
import random

p = 7919

#Get list of all possible Generator values for a given
#prime number for public key generation

def getG(p):

	values = []

	for x in range (1, p):
		rand = x
		exp = 1
		next = rand % p

		while (next != 1 ):
			next = (next * rand) % p
			exp += 1
		

		if (exp == p - 1):
			values.append(rand)

	return values

print(getG(p))