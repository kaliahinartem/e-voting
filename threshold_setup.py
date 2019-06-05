from settings import *
from securegroups import *
from instances import *
from generate_cyclic_group import *

#creates thresholds for number of tellers
def threshold():
	teller_keys = []

	for i in range(tellers):
		teller_keys.append(generate_keys())

	print(teller_keys[0]['pk'].value)

	pkT = 1
	for i in teller_keys:
		pkT *= i['pk'].value

	print(pkT)

threshold()