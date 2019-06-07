import settings

class Parameters:
	p = None,
	g = None,
	q = None

# constructor for elements (storing SK and PK etc.)
class Element(object):
	def __init__(self, type=None, value=None, parameters=settings.parameters):
		self.type = type
		self.value = value
		self.parameters = parameters

class PoK(object):
	def __init__(self, a=None, z=None, parameters=settings.parameters):
		self.c = a
		self.f = z

