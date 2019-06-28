from settings import *
import gmpy2

class Element(object):
	# constructor for elements (storing SK and PK etc.)
	def __init__(self, type=None, value=None, id=None, parameters=parameters):
		self.type = type
		self.value = value
		self.id = id
		self.parameters = parameters

	def __str__(self):
		return 'Element:\n\ttype = %s\n\tvalue = %s\n\tid = %s\n\t' % (str(self.type), str(self.value), str(self.id))

class Keys(object):
	def __init__(self, pk=None, sk=None):
		self.pk = pk
		self.sk = sk

class PoK(object):
	def __init__(self, a=None, z=None, parameters=parameters):
		self.a = a
		self.z = z
		self.parameters = parameters

class Cipher(object):
	def __init__(self, a=None, b=None):
		self.a = a
		self.b = b

class ThresholdKeys(object):
	def __init__(self, pk=None, sk_arr=None, parameters=parameters):
		self.pk = pk
		self.sk_arr = sk_arr
		self.parameters = parameters

	def __str__(self):
		return 'ThresholdKeys:\n\tpublic key = %s\n\tsk_i[0] = %s\n\tsk_i[1] = %s\n\tsk_i[2] = %s' % (str(self.pk.value), str(self.sk_arr[0].value), str(self.sk_arr[1].value), str(self.sk_arr[2].value))

class ThresholdCipher(object):
 #    - v = g^r mod p as in the ElGamal scheme
 #    - c = m * g^r mod p as in the ElGamal scheme with m being the value to be encrypted
 #    - enc the symmetrically encrypted message.
 #    The symmetric key is derived from the ElGamal encrypted value m.
	def __init__(self, v=None, c=None, enc=None):
		self.v = v
		self.c = c
		self.enc = enc

	def __str__(self):
		return 'ThresholdCipher:\n\tv = %s\n\tc = %s\n\tenc = %s' % (str(self.v), str(self.c), str(self.enc))

class PartialDecryption:
	"""
	A partial decryption (x_i, v^(y_i)) of an encrypted message computed by a share owner using his share.
	"""
	def __init__(self, id=None, v_y=None):
		"""
		Construct the partial decryption.
		:param x: the shares x value
		:param v_y: the computed partial decryption value
		"""
		self.id = id
		self.v_y = v_y

	def __str__(self):
		return 'PartialDecryption:\n\tid = %s\n\tv_y = %s' % (str(self.v), str(self.c), str(self.enc))

class Signature(object):
	def __init__(self, k=None, s=None):
		self.k = k
		self.s = s
		

