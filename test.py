def myfun(*args):
	saved_args = locals()
	print(type(saved_args['args'][0]))
	print(type(saved_args))

myfun(1, 2)