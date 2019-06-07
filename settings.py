class Parameters:
	p = None,
	g = None,
	q = None

type_G = 0 #element is in the group
type_Z = 1 #element is in the exponent space
security_level = 512
tellers = 3
parameters = Parameters()
print(parameters)

# constructor for elements (storing SK and PK etc.)
class Element(object):
	def __init__(self, type=None, value=None, parameters=parameters):
		self.type = type
		self.value = value
		self.parameters = parameters

class PoK(object):
	def __init__(self, a=None, z=None, parameters=parameters):
		self.a = a
		self.z = z


