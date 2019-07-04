from settings import *
import gmpy2

class El(object):
	"""
	Element in the group/exponent space that stores parameters of the system
	"""
	def __init__(self, type=None, value=None, id=None, parameters=parameters):
		"""
		Construct element.
		:param type: type of element. type_G - element in the group, type_Z - element in the exponent space
		:param value: integer value of the element
		:param id: identification number (may be used for threshold encr identification)
		:param parameters: global parameters of the system
		"""
		self.type = type
		self.value = value
		self.id = id
		self.parameters = parameters

	def __str__(self):
		return 'Element:\n\ttype = %s\n\tvalue = %s\n\tid = %s\n\t' % (str(self.type), str(self.value), str(self.id))

class Keys(object):
	"""
	Store public and private key elements of El class type
	"""
	def __init__(self, pk=None, sk=None):
		"""
		Construct instance storing keys.
		:param pk: public key
		:param sk: secret key
		"""
		self.pk = pk
		self.sk = sk

	def __str__(self):
		return 'Keys:\n\tpk = %s\n\tsk = %s\n\t' % (str(self.pk), str(self.sk))

class PoK(object):
	"""
	Store proof of knowledge of exponent
	"""
	def __init__(self, a=None, z=None, parameters=parameters):
		"""
		Construct instance storing keys.
		:param a: a = g^r mod p
		:param z: z = r + H(g, pk, a) * x
		:param parameters: global parameters of the system
		"""
		self.a = a
		self.z = z
		self.parameters = parameters

class Cipher(object):
	"""
	Elgamal ciphertext with a and b encryption terms.
	"""
	def __init__(self, a=None, b=None):
		"""
		Construct elgamal ciphertext.
		:param a: a = g^r  mod p
		:param b: b = m * pk^r mod p with m being the value to be encrypted.
		"""
		self.a = a
		self.b = b

	def __str__(self):
		return 'Ciphertext:\n\ta = %s\n\tb = %s' % (str(self.a.value), str(self.b.value))

class ThresholdKeys(object):
	"""
	Store threshold keys.
	"""
	def __init__(self, pk=None, sk_arr=None, parameters=parameters):
		"""
		:param pk: elections public key.
		:param sk_arr: array of secret share keys of tellers.
		:param parameters: global parameters of the system
		"""
		self.pk = pk
		self.sk_arr = sk_arr
		self.parameters = parameters

	def __str__(self):
		return 'ThresholdKeys:\n\tpublic key = %s\n\tsk_i[0] = %s\n\tsk_i[1] = %s\n\tsk_i[2] = %s' % (str(self.pk.value), str(self.sk_arr[0].value), str(self.sk_arr[1].value), str(self.sk_arr[2].value))

class ThresholdCipher(object):
	"""
	Store treshold ciphertext.
	"""
	def __init__(self, v=None, c=None, enc=None):
		"""
		Construct threshold ciphers.
		:param v: v = g^r mod p as in the ElGamal scheme.
		:param c: c = m * g^r mod p as in the ElGamal scheme with m being the value to be encrypted.
		:param enc: the symmetrically encrypted message.
		The symmetric key is derived from the ElGamal encrypted value m.
		"""
		self.v = v
		self.c = c
		self.enc = enc

	def __str__(self):
		return 'ThresholdCipher:\n\tv = %s\n\tc = %s\n\tenc = %s' % (str(self.v), str(self.c), str(self.enc))

class ThresholdParameters:
    """
    Contains the parameters used for the threshold scheme:
    - t: number of share owners required to decrypt a message
    - n: number of share owners involved

    In other words:
    At least t out of overall n share owners must participate to decrypt an encrypted message.
    """
    def __init__(self, t=None, n=None):
        """
        Construct threshold parameter. Required:
        0 < t <= n

        :param t: number of share owners required for decryption
        :param n: overall number of share owners
        """
        if t > n:
            raise ThresholdCryptoError('threshold parameter t must be smaller than n')
        if t <= 0:
            raise ThresholdCryptoError('threshold parameter t must be greater than 0')

        self.t = t
        self.n = n

    def __str__(self):
        return 'ThresholdParameters: t = %d, n = %d)' % (self.t, self.n)


class PartialDecryption:
	"""
	A partial decryption (x_i, v^(y_i)) of an encrypted message computed by a share owner using his share.
	"""
	def __init__(self, id=None, v_y=None):
		"""
		Construct the partial decryption.
		:param id: the shares id value
		:param v_y: the computed partial decryption value
		"""
		self.id = id
		self.v_y = v_y

	def __str__(self):
		return 'PartialDecryption:\n\tid = %s\n\tv_y = %s' % (str(self.v), str(self.c), str(self.enc))

class Signature(object):
	"""
	Store signature.
	"""
	def __init__(self, k=None, s=None):
		"""
		Construct signature terms.
		:param k: k = g^r
		:parak s: s = r + H(m) * sk, where m is a message to be signed
		"""
		self.k = k
		self.s = s

	def __str__(self):
		return 'Signature:\n\tk = %s\n\ts = %s' % (str(self.k.value), str(self.s.value))

