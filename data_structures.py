from settings import *

# constructor for elements (storing SK and PK etc.)
class Element(object):
	def __init__(self, type=None, value=None, parameters=parameters):
		self.type = type
		self.value = value
		self.parameters = parameters

class Keys(object):
	def __init__(self, pk=None, sk=None):
		self.pk = pk
		self.sk = sk

class PoK(object):
	def __init__(self, a=None, z=None, parameters=parameters):
		self.a = a
		self.z = z

class Cipher(object):
	def __init__(self, a=None, b=None):
		self.a = a
		self.b = b