#!/bin/pysh
def python(args:list = []):
	# A lacking Python interpreter
	# Users do not have root Python access
	while True:
		cmd = input('>>> ')
		if cmd.startswith('exit'):
			break
		elif cmd.startswith('help'):
			func = globals()
			del func['__builtins__']
			print('\n'.join(func))
		else:
			try:
				exec(cmd)
			except Exception as e:
				print(f'{shell}: {inspect.stack()[0][3]}: {e}')
	return
