from settings import *
from data_structures import *
from threshold_crypto import (ThresholdCrypto, ThresholdParameters)

#creates public key and shared keys for number of tellers
def threshold():
	global parameters, tellers
	thresh_params = ThresholdParameters(tellers, tellers)
	pub_key, key_shares = ThresholdCrypto.create_public_key_and_shares_centralized(parameters, thresh_params)
	PK = Element(type_G, pub_key.g_a)
	print(type(key_shares))

	return PK, key_shares

threshold()