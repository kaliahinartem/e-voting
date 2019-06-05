from settings import *

# constructor for elements (storing SK and PK etc.)
class Element(object):
	def __init__(self, type=None, value=None, parameters=parameters):
		self.type = type
		self.value = value
		self.parameters = parameters