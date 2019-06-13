class Parameters:
	p = None,
	g = None,
	q = None

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
		
type_G = 0 #element is in the group
type_Z = 1 #element is in the exponent space
security_level = 512
tellers = 3
parameters = Parameters()

#test!! parameters
parameters.p = 19305903377918504234644571620401875817331760586110570595520480093810293868972888209674086377348699019232495477695433624750552102068492069355914600302950327
parameters.g = 4253031672228858798817226538161334555621828462247237901238390265256702460675223577522610183598946302905635480218201409702966504177685363616836699424843483
parameters.q = 9652951688959252117322285810200937908665880293055285297760240046905146934486444104837043188674349509616247738847716812375276051034246034677957300151475163
